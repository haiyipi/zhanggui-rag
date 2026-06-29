"""
图片处理节点（完整版）
处理 Markdown 中的图片：上传到 MinIO，生成图片描述
"""
import os
import sys
import re
import base64
from pathlib import Path
from typing import List, Tuple, Dict
from collections import deque
import time

from app.core.logger import logger
from app.import_process.agent.state import ImportGraphState
from app.utils.task_utils import add_running_task, add_done_task
from app.clients.minio_utils import get_minio_client
from app.conf.minio_config import minio_config
from app.lm.lm_utils import get_llm_client
from app.conf.lm_config import lm_config
from app.core.load_prompt import load_prompt
from app.utils.rate_limit_utils import apply_api_rate_limit


# 支持的图片格式
IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"}


def node_md_img(state: ImportGraphState) -> ImportGraphState:
    """
    MD文件图片处理节点（完整版）

    核心流程：
        1. 获取MD内容和图片目录
        2. 扫描MD中引用的图片
        3. 调用多模态大模型生成图片摘要
        4. 上传图片到MinIO并替换MD中的路径
        5. 保存处理后的MD文件

    Args:
        state: 导入流程状态

    Returns:
        更新后的状态
    """
    func_name = sys._getframe().f_code.co_name
    logger.info(f">>> 开始执行节点: {func_name}")

    add_running_task(state.get("task_id", ""), func_name)

    try:
        # 步骤1：获取MD内容
        md_path = state.get("md_path", "")
        md_content = state.get("md_content", "")

        if not md_path and not md_content:
            logger.warning("无MD内容，跳过图片处理")
            return state

        # 读取MD内容
        if md_content:
            content = md_content
        else:
            with open(md_path, "r", encoding="utf-8") as f:
                content = f.read()

        # 图片目录（MD文件同级的images文件夹）
        images_dir = Path(md_path).parent / "images" if md_path else None

        if not images_dir or not images_dir.exists():
            logger.info(f"图片目录不存在，跳过处理: {images_dir}")
            return state

        # 步骤2：扫描图片
        targets = step_2_scan_images(content, images_dir)
        if not targets:
            logger.info("未找到需要处理的图片")
            return state

        logger.info(f"找到 {len(targets)} 张图片需要处理")

        # 步骤3：生成图片摘要
        summaries = step_3_generate_summaries(state.get("file_title", "文档"), targets)

        # 步骤4：上传并替换
        minio_client = get_minio_client()
        if minio_client:
            new_content = step_4_upload_and_replace(
                minio_client,
                state.get("file_title", "doc"),
                targets,
                summaries,
                content
            )
            state["md_content"] = new_content

            # 步骤5：保存新文件
            if md_path:
                new_md_path = Path(md_path).parent / f"{Path(md_path).stem}_new.md"
                with open(new_md_path, "w", encoding="utf-8") as f:
                    f.write(new_content)
                logger.info(f"处理后的MD已保存: {new_md_path}")
                state["md_path"] = str(new_md_path)
        else:
            logger.warning("MinIO客户端未初始化，跳过图片上传")

    except Exception as e:
        logger.error(f"图片处理失败: {e}", exc_info=True)

    finally:
        add_done_task(state.get("task_id", ""), func_name)
        logger.info(f">>> 节点执行完成: {func_name}")

    return state


def is_supported_image(filename: str) -> bool:
    """判断是否为支持的图片格式"""
    return os.path.splitext(filename)[1].lower() in IMAGE_EXTENSIONS


def find_image_in_md(md_content: str, image_filename: str, context_len: int = 100) -> List[Tuple[str, str]]:
    """查找MD中图片的上下文"""
    pattern = re.compile(r"!\[.*?\]\(.*?" + re.escape(image_filename) + r".*?\)")
    results = []

    for m in pattern.finditer(md_content):
        start, end = m.span()
        pre_text = md_content[max(0, start - context_len):start]
        post_text = md_content[end:min(len(md_content), end + context_len)]
        results.append((pre_text.strip(), post_text.strip()))

    return results


def step_2_scan_images(md_content: str, images_dir: Path) -> List[Tuple[str, str, Tuple[str, str]]]:
    """扫描MD中引用的图片"""
    targets = []

    for image_file in os.listdir(images_dir):
        if not is_supported_image(image_file):
            continue

        img_path = str(images_dir / image_file)
        context_list = find_image_in_md(md_content, image_file)

        if not context_list:
            logger.debug(f"图片未在MD中引用，跳过: {image_file}")
            continue

        targets.append((image_file, img_path, context_list[0]))
        logger.debug(f"发现图片: {image_file}")

    return targets


def encode_image_to_base64(image_path: str) -> str:
    """将图片编码为Base64"""
    with open(image_path, "rb") as img_file:
        base64_str = base64.b64encode(img_file.read()).decode("utf-8")
    return base64_str


def step_3_generate_summaries(
    doc_stem: str,
    targets: List[Tuple[str, str, Tuple[str, str]]],
    requests_per_minute: int = 9
) -> Dict[str, str]:
    """生成图片摘要"""
    summaries = {}
    request_times = deque()

    try:
        # 获取多模态模型客户端
        vlm_client = get_llm_client(model=lm_config.lv_model)
    except Exception as e:
        logger.warning(f"VLM客户端初始化失败: {e}，使用默认描述")
        for img_file, _, _ in targets:
            summaries[img_file] = "图片描述"
        return summaries

    for img_file, img_path, context in targets:
        try:
            # 速率限制
            apply_api_rate_limit(request_times, requests_per_minute, window_seconds=60)

            # 读取并编码图片
            base64_image = encode_image_to_base64(img_path)

            # 加载提示词
            prompt = load_prompt(
                "image_summary",
                root_folder=doc_stem,
                image_content=context
            )

            # 调用VLM
            from langchain.messages import HumanMessage

            message = HumanMessage(
                content=[
                    {"type": "text", "text": prompt},
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}
                    }
                ]
            )

            response = vlm_client.invoke([message])
            summary = response.content.strip().replace("\n", "")[:100]

            if not summary:
                summary = "图片描述"

            summaries[img_file] = summary
            logger.info(f"图片摘要生成: {img_file} -> {summary[:50]}...")

        except Exception as e:
            logger.error(f"图片摘要生成失败 {img_file}: {e}")
            summaries[img_file] = "图片描述"

    return summaries


def step_4_upload_and_replace(
    minio_client,
    doc_stem: str,
    targets: List[Tuple[str, str, Tuple[str, str]]],
    summaries: Dict[str, str],
    md_content: str
) -> str:
    """上传图片到MinIO并替换MD中的引用"""
    upload_dir = f"{minio_config.minio_img_dir}/{doc_stem}".replace(" ", "")
    bucket = minio_config.bucket_name
    protocol = "https" if minio_config.minio_secure else "http"

    for img_file, img_path, _ in targets:
        try:
            # 上传图片
            object_name = f"{upload_dir}/{img_file}"
            minio_client.fput_object(bucket, object_name, img_path)

            # 构造URL
            img_url = f"{protocol}://{minio_config.endpoint}/{bucket}{object_name}"
            img_url = img_url.replace("\\", "%5C")

            # 获取摘要
            summary = summaries.get(img_file, "图片")

            # 替换MD中的引用
            pattern = re.compile(
                r"!\[.*?\]\(.*?" + re.escape(img_file) + r".*?\)",
                re.IGNORECASE
            )
            md_content = pattern.sub(f"![{summary}]({img_url})", md_content)

            logger.info(f"图片已上传: {img_file} -> {img_url}")

        except Exception as e:
            logger.error(f"图片上传失败 {img_file}: {e}")

    return md_content


# ==================== 测试代码 ====================
if __name__ == "__main__":
    from app.utils.path_util import PROJECT_ROOT

    print("\n" + "=" * 50)
    print("测试 node_md_img 节点（完整版）")
    print("=" * 50)

    # 创建测试MD文件
    test_md_dir = PROJECT_ROOT / "output" / "test_md_img"
    test_md_dir.mkdir(parents=True, exist_ok=True)

    test_md_path = test_md_dir / "test_doc.md"
    test_content = """# 测试文档

## 产品图片

这是一张产品图片：

![产品图](images/product.jpg)

## 说明

这是测试内容。
"""
    with open(test_md_path, "w", encoding="utf-8") as f:
        f.write(test_content)

    # 创建图片目录和测试图片
    images_dir = test_md_dir / "images"
    images_dir.mkdir(exist_ok=True)

    # 创建一个简单的1x1像素JPEG图片
    test_img_path = images_dir / "product.jpg"
    if not test_img_path.exists():
        # 最小的有效JPEG文件
        minimal_jpeg = bytes([
            0xFF, 0xD8, 0xFF, 0xDB, 0x00, 0x43, 0x00, 0x08, 0x06, 0x06, 0x07, 0x06, 0x05, 0x08, 0x07, 0x07,
            0x07, 0x09, 0x09, 0x08, 0x0A, 0x0C, 0x14, 0x0D, 0x0C, 0x0B, 0x0B, 0x0C, 0x19, 0x12, 0x13, 0x0F,
            0x14, 0x1D, 0x1A, 0x1F, 0x1E, 0x1D, 0x1A, 0x1C, 0x1C, 0x20, 0x24, 0x2E, 0x27, 0x20, 0x22, 0x2C,
            0x23, 0x1C, 0x1C, 0x28, 0x37, 0x29, 0x2C, 0x30, 0x31, 0x34, 0x34, 0x34, 0x1F, 0x27, 0x39, 0x3D,
            0x38, 0x32, 0x3C, 0x2E, 0x33, 0x34, 0x32, 0xFF, 0xC0, 0x00, 0x11, 0x08, 0x00, 0x01, 0x00, 0x01,
            0x03, 0x01, 0x22, 0x00, 0x02, 0x11, 0x01, 0x03, 0x11, 0x01, 0xFF, 0xC4, 0x00, 0x15, 0x00, 0x01,
            0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x08, 0xFF,
            0xC4, 0x00, 0x14, 0x10, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
            0x00, 0x00, 0x00, 0x00, 0xFF, 0xDA, 0x00, 0x0C, 0x03, 0x01, 0x00, 0x02, 0x10, 0x03, 0x10, 0x00,
            0x00, 0x01, 0x95, 0xFF, 0xD9
        ])
        with open(test_img_path, "wb") as f:
            f.write(minimal_jpeg)

    # 创建测试状态
    test_state = {
        "task_id": "test_md_img_full_001",
        "file_title": "test_doc",
        "md_path": str(test_md_path),
        "md_content": "",
        "local_dir": str(test_md_dir),
        "is_stream": False
    }

    try:
        result = node_md_img(test_state)

        print(f"\n✅ 测试完成")
        print(f"   MD路径: {result.get('md_path')}")
        print(f"   MD内容长度: {len(result.get('md_content', ''))} 字符")

        # 检查图片是否被替换
        new_content = result.get('md_content', '')
        if "minio" in new_content.lower() or "localhost" in new_content.lower():
            print(f"   ✅ 图片URL已替换为MinIO地址")
        else:
            print(f"   ⚠️ 图片未替换（MinIO可能未连接）")

    except Exception as e:
        print(f"\n❌ 测试失败: {e}")
        import traceback
        traceback.print_exc()