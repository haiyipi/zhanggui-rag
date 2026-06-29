"""
HyDE (Hypothetical Document Embeddings) 检索节点
先让LLM生成假设性答案，再用答案进行向量检索
"""
import sys

from app.core.logger import logger
from app.query_process.agent.state import QueryGraphState
from app.utils.task_utils import add_running_task, add_done_task
from app.lm.lm_utils import get_llm_client
from app.lm.embedding_utils import generate_embeddings
from app.clients.milvus_utils import get_milvus_client, hybrid_search, create_hybrid_search_requests


def node_search_embedding_hyde(state: QueryGraphState) -> QueryGraphState:
    """
    HyDE检索节点

    原理：
        1. 让LLM根据用户问题生成一段假设性的理想答案
        2. 将假设答案向量化
        3. 用假设答案的向量去检索真实文档
        4. 返回检索结果

    优点：解决短查询语义稀疏问题，提高召回率
    """
    func_name = sys._getframe().f_code.co_name
    logger.info(f">>> 开始执行节点: {func_name}")

    add_running_task(state.get("session_id", ""), func_name, state.get("is_stream", False))

    query = state.get("rewritten_query", "") or state.get("original_query", "")
    item_names = state.get("item_names", [])

    if not query:
        logger.warning("查询为空，跳过HyDE检索")
        state["hyde_embedding_chunks"] = []
        add_done_task(state.get("session_id", ""), func_name, state.get("is_stream", False))
        return state

    try:
        # 步骤1：生成假设性文档
        logger.info(f"生成假设性文档: {query[:50]}...")
        hyde_doc = step_generate_hypothetical_doc(query)

        if not hyde_doc:
            logger.warning("假设性文档生成失败，跳过HyDE检索")
            state["hyde_embedding_chunks"] = []
            add_done_task(state.get("session_id", ""), func_name, state.get("is_stream", False))
            return state

        logger.info(f"假设性文档长度: {len(hyde_doc)} 字符")

        # 步骤2：向量化假设性文档
        embeddings = generate_embeddings([hyde_doc])
        dense_vec = embeddings.get("dense")[0]
        sparse_vec = embeddings.get("sparse")[0]

        # 步骤3：构建过滤条件
        expr = None
        if item_names and item_names != ["通用"]:
            quoted = ", ".join(f'"{v}"' for v in item_names)
            expr = f"item_name in [{quoted}]"
            logger.info(f"过滤条件: {expr}")

        # 步骤4：连接Milvus
        client = get_milvus_client()
        if not client:
            logger.warning("Milvus未连接，返回空结果")
            state["hyde_embedding_chunks"] = []
            add_done_task(state.get("session_id", ""), func_name, state.get("is_stream", False))
            return state

        # 步骤5：执行混合搜索
        from app.conf.milvus_config import milvus_config
        reqs = create_hybrid_search_requests(
            dense_vector=dense_vec,
            sparse_vector=sparse_vec,
            expr=expr,
            limit=10
        )

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
        state["hyde_embedding_chunks"] = chunks
        state["hyde_doc"] = hyde_doc
        logger.info(f"HyDE检索到 {len(chunks)} 个相关切片")

    except Exception as e:
        logger.error(f"HyDE检索失败: {e}", exc_info=True)
        state["hyde_embedding_chunks"] = []
        state["hyde_doc"] = ""

    add_done_task(state.get("session_id", ""), func_name, state.get("is_stream", False))
    logger.info(f">>> 节点执行完成: {func_name}")

    return state


def step_generate_hypothetical_doc(query: str) -> str:
    """
    生成假设性文档

    Args:
        query: 用户问题

    Returns:
        假设性的理想答案
    """
    try:
        llm = get_llm_client()

        prompt = f"""请根据以下用户问题，生成一段假设性的理想回答。

用户问题：{query}

要求：
1. 回答要具体、专业，包含关键信息
2. 假设你是该领域的专家
3. 不要使用"可能"、"也许"等不确定词汇
4. 300字以内

假设性回答："""

        response = llm.invoke(prompt)
        hyde_doc = response.content.strip()

        return hyde_doc

    except Exception as e:
        logger.error(f"生成假设性文档失败: {e}")
        return ""