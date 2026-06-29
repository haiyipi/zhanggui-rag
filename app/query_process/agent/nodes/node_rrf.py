"""
RRF融合排序节点
将多路召回的结果进行融合排序
"""
import sys
from typing import List, Dict, Any, Tuple

from app.core.logger import logger
from app.query_process.agent.state import QueryGraphState
from app.utils.task_utils import add_running_task, add_done_task


def node_rrf(state: QueryGraphState) -> QueryGraphState:
    """
    RRF (Reciprocal Rank Fusion) 融合排序节点

    功能：
        1. 合并多路召回结果（向量检索、HyDE检索、联网搜索）
        2. 使用RRF算法重新排序
        3. 去重并返回Top-K结果
    """
    func_name = sys._getframe().f_code.co_name
    logger.info(f">>> 开始执行节点: {func_name}")

    add_running_task(state.get("session_id", ""), func_name, state.get("is_stream", False))

    # 获取各路召回结果
    embedding_chunks = state.get("embedding_chunks", [])
    hyde_chunks = state.get("hyde_embedding_chunks", [])
    web_docs = state.get("web_search_docs", [])

    logger.info(f"RRF输入: 向量检索={len(embedding_chunks)}, HyDE检索={len(hyde_chunks)}, 联网搜索={len(web_docs)}")

    # 如果没有结果，直接返回
    if not embedding_chunks and not hyde_chunks and not web_docs:
        state["rrf_chunks"] = []
        add_done_task(state.get("session_id", ""), func_name, state.get("is_stream", False))
        return state

    # 标准化文档格式
    norm_embedding = _normalize_chunks(embedding_chunks, "embedding")
    norm_hyde = _normalize_chunks(hyde_chunks, "hyde")
    norm_web = _normalize_web_docs(web_docs)

    # RRF融合（可调整权重）
    source_weights = [
        (norm_embedding, 1.0),
        (norm_hyde, 0.8),
        (norm_web, 0.6),
    ]

    fused_results = _reciprocal_rank_fusion(source_weights, k=60, max_results=10)

    # 提取文档列表
    rrf_chunks = [doc for doc, score in fused_results]

    state["rrf_chunks"] = rrf_chunks
    logger.info(f"RRF输出: {len(rrf_chunks)} 个文档")

    add_done_task(state.get("session_id", ""), func_name, state.get("is_stream", False))
    logger.info(f">>> 节点执行完成: {func_name}")

    return state


def _normalize_chunks(chunks: List[Dict], source: str) -> List[Dict]:
    """标准化文档格式"""
    result = []
    for i, chunk in enumerate(chunks):
        if not chunk:
            continue
        if isinstance(chunk, dict):
            doc_id = chunk.get("chunk_id") or chunk.get("id") or f"{source}_{i}"
            content = chunk.get("content", "")
            if not content and "entity" in chunk:
                content = chunk["entity"].get("content", "")
            score = chunk.get("distance", chunk.get("score", 0.0))
            result.append({
                "id": str(doc_id),
                "content": content,
                "score": score,
                "source": source,
                "raw": chunk
            })
        elif hasattr(chunk, "entity"):
            doc_id = getattr(chunk, "id", f"{source}_{i}")
            entity = getattr(chunk, "entity", {})
            content = entity.get("content", "") if isinstance(entity, dict) else ""
            result.append({
                "id": str(doc_id),
                "content": content,
                "score": getattr(chunk, "distance", 0.0),
                "source": source,
                "raw": chunk
            })
    return result


def _normalize_web_docs(docs: List[Dict]) -> List[Dict]:
    """标准化联网搜索结果格式"""
    result = []
    for i, doc in enumerate(docs):
        content = doc.get("snippet", doc.get("content", ""))
        if content:
            result.append({
                "id": f"web_{i}",
                "content": content,
                "score": 0.5,
                "source": "web",
                "raw": doc,
                "title": doc.get("title", ""),
                "url": doc.get("url", "")
            })
    return result


def _reciprocal_rank_fusion(
        source_weights: List[Tuple[List[Dict], float]],
        k: int = 60,
        max_results: int = None
) -> List[Tuple[Dict, float]]:
    """带权重的RRF算法"""
    score_map = {}
    doc_map = {}

    for docs, weight in source_weights:
        for rank, doc in enumerate(docs, start=1):
            doc_id = doc.get("id", "")
            if not doc_id:
                continue
            rrf_score = weight * (1.0 / (k + rank))
            score_map[doc_id] = score_map.get(doc_id, 0.0) + rrf_score
            if doc_id not in doc_map:
                doc_map[doc_id] = doc

    merged = [(doc_map[doc_id], score) for doc_id, score in score_map.items()]
    merged.sort(key=lambda x: x[1], reverse=True)

    if max_results:
        merged = merged[:max_results]

    return merged