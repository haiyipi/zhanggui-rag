"""
重排序节点
"""
import sys
from app.core.logger import logger
from app.query_process.agent.state import QueryGraphState
from app.utils.task_utils import add_running_task, add_done_task
from app.lm.reranker_utils import rerank


def node_rerank(state: QueryGraphState) -> QueryGraphState:
    """重排序节点"""
    func_name = sys._getframe().f_code.co_name
    logger.info(f">>> 开始执行节点: {func_name}")

    add_running_task(state.get("session_id", ""), func_name, state.get("is_stream", False))

    # 获取待重排的文档
    rrf_chunks = state.get("rrf_chunks", [])
    query = state.get("rewritten_query", "") or state.get("original_query", "")

    if not rrf_chunks or not query:
        logger.warning(f"无待重排文档或查询为空")
        state["reranked_docs"] = rrf_chunks[:10]
        add_done_task(state.get("session_id", ""), func_name, state.get("is_stream", False))
        return state

    logger.info(f"开始重排序: {len(rrf_chunks)} 个文档")

    # 调用 Rerank
    reranked_docs = rerank(query, rrf_chunks)

    # 动态 TopK 截断（取前5个）
    topk_docs = reranked_docs[:5]

    state["reranked_docs"] = topk_docs
    logger.info(f"重排序完成: 输入{len(rrf_chunks)} -> 输出{len(topk_docs)}")

    add_done_task(state.get("session_id", ""), func_name, state.get("is_stream", False))
    logger.info(f">>> 节点执行完成: {func_name}")

    return state