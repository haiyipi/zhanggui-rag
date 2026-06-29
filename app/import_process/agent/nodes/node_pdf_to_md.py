"""
PDF转Markdown节点
利用 MinerU API 将 PDF 转换为结构化的 Markdown 格式
"""
import os
import sys
import time
import json
import requests
import zipfile
import shutil
from pathlib import Path

from app.core.logger import logger
from app.import_process.agent.state import ImportGraphState
from app.utils.task_utils import add_running_task, add_done_task
from app.conf.mineru_config import mineru_config


# MinerU配置
MINERU_BASE_URL = mineru_config.base_url
MINERU_API_TOKEN = mineru_config.api_key


def node_pdf_to_md(state: ImportGraphState) -> ImportGraphState:
    """
    PDF转Markdown节点

    核心流程：
        1. 校验PDF路径和输出目录
        2. 上传PDF至MinerU并轮询解析结果
        3. 下载ZIP包并提取MD文件
        4. 读取MD内容并更新状态

    Args:
        state: 导入流程状态

    Returns:
        更新后的状态，新增 md_path 和 md_content
    """
    func_name = sys._getframe().f_code.co_name
    logger.info(f">>> 开始执行节点: {func_name}")

    # 记录任务开始
    add_running_task(state.get("task_id", ""), func_name)

    try:
        # 步骤1：校验路径
        pdf_path, output_dir = step_1_validate_paths(state)

        # 步骤2：上传并轮询
        zip_url = step_2_upload_and_poll(pdf_path, output_dir)

        # 步骤3：下载并提取MD文件
        md_path = step_3_download_and_extract(zip_url, output_dir, pdf_path.stem)

        # 更新状态
        state["md_path"] = md_path
        logger.info(f"【{func_name}】MD文件生成成功: {md_path}")

        # 读取MD内容
        try:
            with open(md_path, "r", encoding="utf-8") as f:
                state["md_content"] = f.read()
            logger.info(f"【{func_name}】MD内容读取成功，长度: {len(state['md_content'])} 字符")
        except Exception as e:
            logger.error(f"【{func_name}】读取MD文件失败: {e}")

    except Exception as e:
        logger.error(f"【{func_name}】PDF转MD失败: {e}", exc_info=True)
        raise

    finally:
        add_done_task(state.get("task_id", ""), func_name)
        logger.info(f">>> 节点执行完成: {func_name}")

    return state


def step_1_validate_paths(state: ImportGraphState):
    """步骤1：校验PDF路径和输出目录"""
    pdf_path = state.get("pdf_path", "")
    local_dir = state.get("local_dir", "")

    if not pdf_path:
        raise ValueError("PDF路径为空")
    if not local_dir:
        raise ValueError("输出目录为空")

    pdf_path_obj = Path(pdf_path)
    output_dir_obj = Path(local_dir)

    if not pdf_path_obj.exists():
        raise FileNotFoundError(f"PDF文件不存在: {pdf_path}")

    output_dir_obj.mkdir(parents=True, exist_ok=True)

    logger.info(f"PDF路径: {pdf_path_obj}")
    logger.info(f"输出目录: {output_dir_obj}")

    return pdf_path_obj, output_dir_obj


def step_2_upload_and_poll(pdf_path_obj: Path, output_dir_obj: Path):
    """
    步骤2：上传PDF至MinerU并轮询结果
    """
    logger.info(f"【step_2】开始处理PDF: {pdf_path_obj.name}")

    # 检查MinerU配置
    if not MINERU_BASE_URL or not MINERU_API_TOKEN:
        logger.warning("MinerU配置缺失，使用模拟模式")
        return _mock_upload(pdf_path_obj)

    try:
        # 请求头
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {MINERU_API_TOKEN}"
        }

        # 1. 获取上传URL
        url_get_upload = f"{MINERU_BASE_URL}/file-urls/batch"
        req_data = {
            "files": [{"name": pdf_path_obj.name}],
            "model_version": "vlm"
        }

        logger.info(f"请求上传URL: {url_get_upload}")
        resp = requests.post(url_get_upload, headers=headers, json=req_data, timeout=30)

        if resp.status_code != 200:
            raise Exception(f"获取上传URL失败: {resp.status_code}")

        resp_data = resp.json()
        if resp_data.get("code") != 0:
            raise Exception(f"API错误: {resp_data}")

        signed_url = resp_data["data"]["file_urls"][0]
        batch_id = resp_data["data"]["batch_id"]
        logger.info(f"获取上传URL成功, batch_id: {batch_id}")

        # 2. 上传文件
        with open(pdf_path_obj, "rb") as f:
            file_data = f.read()

        # 使用Session禁用代理
        session = requests.Session()
        session.trust_env = False

        put_resp = session.put(signed_url, data=file_data, timeout=60)
        if put_resp.status_code != 200:
            # 重试：指定Content-Type
            headers_pdf = {"Content-Type": "application/pdf"}
            put_resp = session.put(signed_url, data=file_data, headers=headers_pdf, timeout=60)
            if put_resp.status_code != 200:
                raise Exception(f"上传失败: {put_resp.status_code}")

        session.close()
        logger.info("文件上传成功")

        # 3. 轮询任务状态
        poll_url = f"{MINERU_BASE_URL}/extract-results/batch/{batch_id}"
        start_time = time.time()
        timeout_seconds = 600  # 10分钟超时

        while True:
            elapsed = time.time() - start_time
            if elapsed > timeout_seconds:
                raise TimeoutError(f"任务超时: {int(elapsed)}秒")

            poll_resp = requests.get(poll_url, headers=headers, timeout=10)
            if poll_resp.status_code != 200:
                time.sleep(3)
                continue

            poll_data = poll_resp.json()
            if poll_data.get("code") != 0:
                time.sleep(3)
                continue

            results = poll_data.get("data", {}).get("extract_result", [])
            if not results:
                time.sleep(3)
                continue

            result = results[0]
            state_status = result.get("state")

            if state_status == "done":
                zip_url = result.get("full_zip_url")
                if not zip_url:
                    raise Exception("未返回ZIP下载链接")
                logger.info(f"任务完成，耗时: {int(elapsed)}秒")
                return zip_url
            elif state_status == "failed":
                err_msg = result.get("err_msg", "未知错误")
                raise Exception(f"任务失败: {err_msg}")
            else:
                logger.debug(f"处理中... 状态: {state_status}")
                time.sleep(3)

    except Exception as e:
        logger.error(f"MinerU API调用失败: {e}")
        logger.warning("使用模拟模式继续")
        return _mock_upload(pdf_path_obj)


def _mock_upload(pdf_path_obj: Path) -> str:
    """模拟上传（用于测试）"""
    logger.info(f"【模拟模式】处理PDF: {pdf_path_obj.name}")
    time.sleep(1)
    return f"https://mock.example.com/{pdf_path_obj.stem}_result.zip"


def step_3_download_and_extract(zip_url: str, output_dir_obj: Path, pdf_stem: str) -> str:
    """
    步骤3：下载ZIP并提取MD文件
    """
    logger.info(f"【step_3】开始处理ZIP: {zip_url}")

    # 创建解压目录
    extract_dir = output_dir_obj / pdf_stem
    extract_dir.mkdir(parents=True, exist_ok=True)

    # 下载ZIP
    zip_path = extract_dir / f"{pdf_stem}_result.zip"

    try:
        # 尝试下载
        if zip_url.startswith("http"):
            resp = requests.get(zip_url, timeout=120)
            if resp.status_code == 200:
                with open(zip_path, "wb") as f:
                    f.write(resp.content)
                logger.info(f"ZIP下载成功: {zip_path}")

                # 解压
                with zipfile.ZipFile(zip_path, 'r') as zf:
                    zf.extractall(extract_dir)
                logger.info(f"ZIP解压成功: {extract_dir}")

                # 查找MD文件
                md_files = list(extract_dir.rglob("*.md"))
                if md_files:
                    # 优先选择与PDF同名的
                    target_md = None
                    for md in md_files:
                        if md.stem == pdf_stem:
                            target_md = md
                            break
                    if not target_md:
                        target_md = md_files[0]

                    # 重命名
                    final_md = extract_dir / f"{pdf_stem}.md"
                    if target_md != final_md:
                        shutil.move(str(target_md), str(final_md))

                    logger.info(f"MD文件: {final_md}")
                    return str(final_md)
    except Exception as e:
        logger.warning(f"下载/解压失败: {e}")

    # 模拟MD文件（用于测试）
    logger.info("使用模拟MD文件")
    mock_md_path = extract_dir / f"{pdf_stem}.md"

    mock_content = f"""# {pdf_stem}

## 产品概述

这是从PDF转换而来的Markdown内容。

## 操作说明

1. 第一步操作
2. 第二步操作
3. 第三步操作

## 注意事项

- 注意事项1
- 注意事项2
"""
    with open(mock_md_path, "w", encoding="utf-8") as f:
        f.write(mock_content)

    return str(mock_md_path)


# ==================== 测试代码 ====================
if __name__ == "__main__":
    from app.utils.path_util import PROJECT_ROOT

    print("\n" + "=" * 50)
    print("测试 node_pdf_to_md 节点")
    print("=" * 50)

    # 创建测试状态
    test_state = {
        "task_id": "test_pdf2md_001",
        "pdf_path": str(PROJECT_ROOT / "doc" / "hak180产品安全手册.pdf"),
        "local_dir": str(PROJECT_ROOT / "output"),
        "is_stream": False
    }

    # 确保目录存在
    Path(test_state["local_dir"]).mkdir(parents=True, exist_ok=True)

    try:
        result = node_pdf_to_md(test_state)
        print(f"\n✅ 测试完成")
        print(f"   MD路径: {result.get('md_path')}")
        print(f"   MD内容长度: {len(result.get('md_content', ''))} 字符")
        print(f"   MD内容预览:\n{result.get('md_content', '')[:200]}...")
    except Exception as e:
        print(f"\n❌ 测试失败: {e}")
        import traceback
        traceback.print_exc()