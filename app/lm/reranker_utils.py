"""
Reranker 工具类 - 使用本地模型（强制离线）
"""
import os

# ==================== 必须在导入 FlagReranker 之前设置 ====================
os.environ['TRANSFORMERS_OFFLINE'] = '1'
os.environ['HF_HUB_OFFLINE'] = '1'
os.environ['HF_HOME'] = 'D:/ai_models/huggingface_cache'
# ==========================================================================

from FlagEmbedding import FlagReranker
from app.conf.reranker_config import reranker_config
from app.core.logger import logger

_reranker_model = None


def get_reranker_model():
    """获取 Reranker 模型单例"""
    global _reranker_model
    if _reranker_model is None:
        model_path = reranker_config.bge_reranker_large
        device = reranker_config.bge_reranker_device
        use_fp16 = reranker_config.bge_reranker_fp16

        logger.info(f"正在加载 Reranker 模型: {model_path}")

        try:
            _reranker_model = FlagReranker(
                model_name_or_path=model_path,
                device=device,
                use_fp16=use_fp16
            )
            logger.info("Reranker 模型加载成功")
        except Exception as e:
            logger.error(f"Reranker 模型加载失败: {e}")
            raise

    return _reranker_model


def rerank(query: str, documents: list) -> list:
    """
    对文档进行重排序

    Args:
        query: 用户查询
        documents: 文档列表，每个元素应包含 'content' 字段

    Returns:
        排序后的文档列表（高分在前）
    """
    if not documents:
        return []

    try:
        model = get_reranker_model()
        texts = [doc.get('content', '') for doc in documents]

        # 构建查询-文档对
        sentence_pairs = [[query, text] for text in texts]

        # 计算相关性得分
        scores = model.compute_score(sentence_pairs)

        # 确保 scores 是列表
        if isinstance(scores, (int, float)):
            scores = [scores]

        # 添加分数并排序
        for doc, score in zip(documents, scores):
            doc['rerank_score'] = float(score)

        documents.sort(key=lambda x: x.get('rerank_score', 0), reverse=True)

        logger.info(f"Rerank 完成，最高分: {documents[0].get('rerank_score', 0):.4f}")
        return documents

    except Exception as e:
        logger.error(f"Rerank 失败: {e}")
        return documents