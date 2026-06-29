"""
答案生成节点
基于检索结果生成最终答案
"""
import sys

from app.core.logger import logger
from app.query_process.agent.state import QueryGraphState
from app.utils.task_utils import add_running_task, add_done_task, set_task_result
from app.utils.sse_utils import push_to_session, SSEEvent
from app.lm.lm_utils import get_llm_client
from app.clients.mongo_history_utils import save_chat_message


def node_answer_output(state: QueryGraphState) -> QueryGraphState:
    """
    答案生成节点

    功能：
        1. 检查是否已有答案（反问场景）
        2. 基于检索结果生成答案
        3. 支持流式输出
        4. 保存到历史记录
    """
    func_name = sys._getframe().f_code.co_name
    logger.info(f">>> 开始执行节点: {func_name}")

    session_id = state.get("session_id", "")
    is_stream = state.get("is_stream", False)

    add_running_task(session_id, func_name, is_stream)

    # 如果已经有答案（如反问），直接返回
    if state.get("answer"):
        logger.info(f"已有答案，跳过生成: {state['answer'][:50]}...")
        add_done_task(session_id, func_name, is_stream)
        return state

    # 构建 Prompt 并生成答案
    answer = step_generate_answer(state)
    state["answer"] = answer

    # 流式输出
    if is_stream:
        push_to_session(session_id, SSEEvent.DELTA, {"delta": answer})
        push_to_session(session_id, SSEEvent.FINAL, {"answer": answer, "status": "completed"})

    # 保存到历史
    save_chat_message(
        session_id=session_id,
        role="assistant",
        text=answer,
        rewritten_query="",
        item_names=state.get("item_names", [])
    )

    set_task_result(session_id, "answer", answer)
    add_done_task(session_id, func_name, is_stream)
    logger.info(f">>> 节点执行完成: {func_name}")

    return state


def step_generate_answer(state: QueryGraphState) -> str:
    """生成答案"""
    query = state.get("rewritten_query", "") or state.get("original_query", "")
    chunks = state.get("embedding_chunks", [])

    # 构建上下文
    context = ""
    for i, chunk in enumerate(chunks[:5]):
        content = chunk.get("entity", {}).get("content", "") if isinstance(chunk, dict) else ""
        if not content and isinstance(chunk, dict):
            content = chunk.get("content", "")
        if content:
            context += f"\n[参考资料{i + 1}]\n{content}\n"

    if not context:
        return "抱歉，没有找到相关的参考资料，请尝试其他问题。"

    # 构建 Prompt
    prompt = f"""你是一个专业的技术客服助手。请根据以下参考资料回答用户的问题。

【参考资料】
{context}

【用户问题】
{query}

【要求】
1. 基于参考资料回答，不要编造
2. 如果资料不足，诚实说明
3. 回答要准确、简洁、专业

【回答】"""

    try:
        llm = get_llm_client()
        response = llm.invoke(prompt)
        return response.content.strip()

    except Exception as e:
        logger.error(f"生成答案失败: {e}")
        return f"生成答案时出错: {e}"