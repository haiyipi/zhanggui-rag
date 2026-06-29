"""
向量检索节点
在Milvus中搜索相关文档切片
"""
import sys

from app.core.logger import logger
from app.query_process.agent.state import QueryGraphState
from app.utils.task_utils import add_running_task, add_done_task
from app.lm.embedding_utils import generate_embeddings
from app.clients.milvus_utils import get_milvus_client, hybrid_search, create_hybrid_search_requests


def node_search_embedding(state: QueryGraphState) -> QueryGraphState:
    """
    向量检索节点

    功能：
        1. 将改写后的问题向量化
        2. 在Milvus中检索相关文档切片
        3. 返回Top-K结果
    """
    func_name = sys._getframe().f_code.co_name
    logger.info(f">>> 开始执行节点: {func_name}")

    add_running_task(state.get("session_id", ""), func_name, state.get("is_stream", False))

    query = state.get("rewritten_query", "") or state.get("original_query", "")
    item_names = state.get("item_names", [])

    if not query:
        logger.warning("查询为空，跳过检索")
        add_done_task(state.get("session_id", ""), func_name, state.get("is_stream", False))
        return state

    try:
        # 1. 向量化查询
        logger.info(f"向量化查询: {query[:50]}...")
        embeddings = generate_embeddings([query])
        dense_vec = embeddings.get("dense")[0]
        sparse_vec = embeddings.get("sparse")[0]

        # 2. 构建过滤条件
        expr = None
        if item_names and item_names != ["通用"]:
            quoted = ", ".join(f'"{v}"' for v in item_names)
            expr = f"item_name in [{quoted}]"
            logger.info(f"过滤条件: {expr}")

        # 3. 连接Milvus
        client = get_milvus_client()
        if not client:
            logger.warning("Milvus未连接，返回空结果")
            state["embedding_chunks"] = []
            add_done_task(state.get("session_id", ""), func_name, state.get("is_stream", False))
            return state

        # 4. 构建搜索请求
        from app.conf.milvus_config import milvus_config
        reqs = create_hybrid_search_requests(
            dense_vector=dense_vec,
            sparse_vector=sparse_vec,
            expr=expr,
            limit=10
        )

        # 5. 执行混合搜索
        res = hybrid_search(
            client=client,
            collection_name=milvus_config.chunks_collection,
            reqs=reqs,
            ranker_weights=(0.8, 0.2),
            norm_score=True,
            limit=5,
            output_fields=["chunk_id", "content", "title", "item_name", "file_title"]
        )

        chunks = res[0] if res else []
        state["embedding_chunks"] = chunks
        logger.info(f"检索到 {len(chunks)} 个相关切片")

    except Exception as e:
        logger.error(f"向量检索失败: {e}", exc_info=True)
        state["embedding_chunks"] = []

    add_done_task(state.get("session_id", ""), func_name, state.get("is_stream", False))
    logger.info(f">>> 节点执行完成: {func_name}")

    return state