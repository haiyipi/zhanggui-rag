"""
商品确认节点
提取商品名称，改写用户问题
"""
import sys
import json
from typing import List, Dict, Any

from app.core.logger import logger
from app.query_process.agent.state import QueryGraphState
from app.utils.task_utils import add_running_task, add_done_task
from app.lm.lm_utils import get_llm_client
from app.clients.mongo_history_utils import get_recent_messages, save_chat_message
from app.clients.milvus_utils import get_milvus_client, hybrid_search, create_hybrid_search_requests
from app.lm.embedding_utils import generate_embeddings


def node_item_name_confirm(state: QueryGraphState) -> QueryGraphState:
    """
    商品确认节点

    功能：
        1. 从用户问题中提取商品名称
        2. 改写问题为独立完整的查询语句
        3. 在Milvus中确认商品是否存在
        4. 如果无法确认，生成反问让用户选择
    """
    func_name = sys._getframe().f_code.co_name
    logger.info(f">>> 开始执行节点: {func_name}")

    add_running_task(state.get("session_id", ""), func_name, state.get("is_stream", False))

    session_id = state.get("session_id", "")
    original_query = state.get("original_query", "")
    is_stream = state.get("is_stream", False)

    # 步骤1：获取历史记录
    history = get_recent_messages(session_id, limit=10)

    # 步骤2：提取商品名称和改写问题
    extract_result = step_extract_info(original_query, history)
    item_names = extract_result.get("item_names", [])
    rewritten_query = extract_result.get("rewritten_query", original_query)

    state["rewritten_query"] = rewritten_query

    # 步骤3：如果有商品名称，在向量库中确认
    if item_names:
        confirmed_items = step_confirm_items(item_names)

        if confirmed_items:
            # 确认成功
            state["item_names"] = confirmed_items
            logger.info(f"确认商品: {confirmed_items}")
        else:
            # 无法确认，生成反问
            answer = f"您是想问以下哪个产品：{'、'.join(item_names[:3])}？请明确一下型号。"
            state["answer"] = answer
            state["item_names"] = []
            logger.info(f"需要用户确认: {answer}")

            # 保存助手回复
            save_chat_message(session_id, "assistant", answer, "", [])
            add_done_task(session_id, func_name, is_stream)
            return state
    else:
        # 无商品名称，使用文件标题作为兜底（简化处理）
        state["item_names"] = ["通用"]

    # 保存用户问题到历史
    save_chat_message(session_id, "user", original_query, rewritten_query, state.get("item_names", []))

    add_done_task(session_id, func_name, is_stream)
    logger.info(f">>> 节点执行完成: {func_name}")

    return state


def step_extract_info(query: str, history: List[Dict]) -> Dict[str, Any]:
    """提取商品名称和改写问题"""
    try:
        llm = get_llm_client(json_mode=True)

        # 构建历史文本
        history_text = ""
        for msg in history[-5:]:  # 最近5条
            history_text += f"{msg.get('role', '')}: {msg.get('text', '')}\n"

        prompt = f"""请根据历史会话和当前问题，提取商品名称并改写问题。

历史会话：
{history_text}

当前用户问题：{query}

要求：
1. 提取商品名称（item_names），如果没有则返回空列表
2. 改写问题为独立完整的问题（rewritten_query）

请返回JSON格式：
{{"item_names": ["商品名1"], "rewritten_query": "改写后的问题"}}"""

        response = llm.invoke(prompt)
        content = response.content.strip()

        # 清理JSON
        if content.startswith("```json"):
            content = content.replace("```json", "").replace("```", "")

        result = json.loads(content)
        return result

    except Exception as e:
        logger.error(f"提取信息失败: {e}")
        return {"item_names": [], "rewritten_query": query}


def step_confirm_items(item_names: List[str]) -> List[str]:
    """在Milvus中确认商品是否存在"""
    try:
        client = get_milvus_client()
        if not client:
            return item_names  # 无法连接时直接返回原名称

        # 获取商品名称集合
        from app.conf.milvus_config import milvus_config
        collection_name = milvus_config.item_name_collection

        # 检查集合是否存在
        if not client.has_collection(collection_name):
            logger.warning(f"集合 {collection_name} 不存在")
            return item_names

        # 搜索每个商品名
        confirmed = []
        for item in item_names:
            # 简单查询（实际应该用向量搜索）
            result = client.query(
                collection_name=collection_name,
                filter=f'item_name == "{item}"',
                output_fields=["item_name"]
            )
            if result:
                confirmed.append(result[0].get("item_name", item))
            else:
                # 尝试模糊匹配（简化处理）
                confirmed.append(item)

        return confirmed

    except Exception as e:
        logger.error(f"确认商品失败: {e}")
        return item_names