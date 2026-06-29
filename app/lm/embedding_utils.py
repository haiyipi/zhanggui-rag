"""
向量生成工具 - 使用本地 BGE-M3 模型
"""
import os
from app.core.logger import logger
from pymilvus.model.hybrid import BGEM3EmbeddingFunction

# 设置 HuggingFace 缓存路径到 D 盘
os.environ['HF_HOME'] = 'D:/ai_models/huggingface_cache'

_bge_m3_ef = None


def get_bge_m3_ef():
    """获取 BGE-M3 模型单例，使用本地模型"""
    global _bge_m3_ef
    if _bge_m3_ef is None:
        # 本地模型路径
        local_model_path = "D:/ai_models/modelscope_cache/BAAI/bge-m3"

        logger.info(f"加载本地 BGE-M3 模型: {local_model_path}")
        _bge_m3_ef = BGEM3EmbeddingFunction(
            model_name=local_model_path,
            device='cpu',           # 使用 CPU
            use_fp16=False,         # CPU 不需要 FP16
            normalize_embeddings=True
        )
        logger.info("BGE-M3 模型加载成功")
    return _bge_m3_ef


def generate_embeddings(texts):
    """
    为文本列表生成稠密+稀疏混合向量嵌入
    """
    if not isinstance(texts, list) or len(texts) == 0:
        raise ValueError("参数texts必须是包含文本的非空列表")

    logger.info(f"开始为 {len(texts)} 条文本生成 BGE-M3 向量...")

    try:
        model = get_bge_m3_ef()
        embeddings = model.encode_documents(texts)

        # 处理稠密向量
        dense_vectors = [emb.tolist() for emb in embeddings['dense']]

        # 处理稀疏向量（CSR 格式转字典）
        sparse_vectors = []
        for i in range(len(texts)):
            indices = embeddings['sparse'].indices[
                embeddings['sparse'].indptr[i]:embeddings['sparse'].indptr[i + 1]
            ].tolist()
            data = embeddings['sparse'].data[
                embeddings['sparse'].indptr[i]:embeddings['sparse'].indptr[i + 1]
            ].tolist()
            sparse_dict = {k: v for k, v in zip(indices, data)}
            sparse_vectors.append(sparse_dict)

        logger.info(f"成功生成 {len(texts)} 条向量（稠密维度: {len(dense_vectors[0])}）")

        return {
            'dense': dense_vectors,
            'sparse': sparse_vectors
        }

    except Exception as e:
        logger.error(f"BGE-M3 向量生成失败: {e}")
        raise