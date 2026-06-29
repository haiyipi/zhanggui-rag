"""
主体识别节点（简化版 - 不依赖 torch/transformers）
识别文档的核心商品/设备名称
"""
import os
import sys
import json
from typing import List, Dict, Any, Tuple

# 添加项目根目录到路径（必须在其他导入之前）
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from app.core.logger import logger
from app.import_process.agent.state import ImportGraphState
from app.utils.task_utils import add_running_task, add_done_task

# 尝试导入 LLM 客户端，如果失败则使用简化模式
try:
    from app.lm.lm_utils import get_llm_client
    LLM_AVAILABLE = True
except Exception as e:
    logger.warning(f"LLM客户端不可用，使用简化模式: {e}")
    LLM_AVAILABLE = False


DEFAULT_ITEM_NAME_CHUNK_K = 5
SINGLE_CHUNK_CONTENT_MAX_LEN = 800
CONTEXT_TOTAL_MAX_CHARS = 2500


def node_item_name_recognition(state: ImportGraphState) -> ImportGraphState:
    """
    主体识别节点（简化版）
    """
    func_name = sys._getframe().f_code.co_name
    logger.info(f">>> 开始执行节点: {func_name}")

    add_running_task(state.get("task_id", ""), func_name)

    try:
        # 步骤1：获取输入
        file_title, chunks = step_1_get_inputs(state)
        if not chunks:
            logger.warning("无切片数据，跳过主体识别")
            return state

        # 步骤2：构建上下文
        context = step_2_build_context(chunks)

        # 步骤3：识别商品名称
        if LLM_AVAILABLE and context:
            item_name = step_3_call_llm(file_title, context)
        else:
            # 简化模式：使用文件标题
            item_name = file_title
            logger.info(f"简化模式，使用文件标题作为商品名称: {item_name}")

        # 步骤4：更新状态
        step_4_update_state(state, chunks, item_name)

        logger.info(f"商品名称识别完成: {item_name}")

    except Exception as e:
        logger.error(f"主体识别失败: {e}", exc_info=True)
        state["item_name"] = state.get("file_title", "未知商品")

    finally:
        add_done_task(state.get("task_id", ""), func_name)
        logger.info(f">>> 节点执行完成: {func_name}")

    return state


def step_1_get_inputs(state: ImportGraphState) -> Tuple[str, List[Dict]]:
    """步骤1：获取输入数据"""
    file_title = state.get("file_title", "")
    chunks = state.get("chunks", [])

    if not file_title and chunks:
        file_title = chunks[0].get("file_title", "")

    logger.info(f"文件标题: {file_title}, 切片数量: {len(chunks)}")
    return file_title, chunks


def step_2_build_context(chunks: List[Dict]) -> str:
    """步骤2：构建上下文"""
    parts = []
    total_chars = 0

    for idx, chunk in enumerate(chunks[:DEFAULT_ITEM_NAME_CHUNK_K]):
        if not isinstance(chunk, dict):
            continue

        title = chunk.get("title", "").strip()
        content = chunk.get("content", "").strip()

        if not content:
            continue

        if len(content) > SINGLE_CHUNK_CONTENT_MAX_LEN:
            content = content[:SINGLE_CHUNK_CONTENT_MAX_LEN]

        piece = f"【切片{idx + 1}】\n标题：{title}\n内容：{content}"
        parts.append(piece)
        total_chars += len(piece)

        if total_chars > CONTEXT_TOTAL_MAX_CHARS:
            break

    context = "\n\n".join(parts)
    logger.info(f"上下文构建完成，长度: {len(context)} 字符")
    return context


def step_3_call_llm(file_title: str, context: str) -> str:
    """步骤3：调用LLM识别商品名称"""
    try:
        llm = get_llm_client()

        prompt = f"""请根据以下文件标题和文档内容，提取这篇文档描述的核心商品名称。

文件标题：{file_title}

文档内容：
{context}

请直接输出商品名称，不要输出其他内容。"""

        logger.info("调用LLM识别商品名称...")
        response = llm.invoke(prompt)

        item_name = response.content.strip()
        item_name = item_name.replace("\n", "").replace("\r", "").strip()

        if not item_name:
            item_name = file_title

        logger.info(f"LLM识别结果: {item_name}")
        return item_name

    except Exception as e:
        logger.error(f"LLM调用失败: {e}")
        return file_title


def step_4_update_state(state: ImportGraphState, chunks: List[Dict], item_name: str):
    """步骤4：更新状态"""
    state["item_name"] = item_name

    for chunk in chunks:
        chunk["item_name"] = item_name

    state["chunks"] = chunks
    logger.info(f"已为 {len(chunks)} 个切片添加商品名称")


# ==================== 测试代码 ====================
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("测试 node_item_name_recognition 节点（简化版）")
    print("=" * 50)

    # 创建测试切片
    test_chunks = [
        {
            "title": "# HAK 180 烫金机使用手册",
            "content": "HAK 180 烫金机是一款高性能烫金设备，适用于纸张、塑料等材料。",
            "file_title": "hak180产品安全手册"
        },
        {
            "title": "## 产品参数",
            "content": "电源：220V，功率：1800W，工作温度：100-200°C",
            "file_title": "hak180产品安全手册"
        }
    ]

    test_state = {
        "task_id": "test_item_name_001",
        "file_title": "hak180产品安全手册",
        "chunks": test_chunks,
        "is_stream": False
    }

    try:
        result = node_item_name_recognition(test_state)

        print(f"\n✅ 测试完成")
        print(f"   商品名称: {result.get('item_name')}")

        if result.get('chunks'):
            first_chunk = result['chunks'][0]
            print(f"   切片商品名: {first_chunk.get('item_name')}")

    except Exception as e:
        print(f"\n❌ 测试失败: {e}")
        import traceback
        traceback.print_exc()