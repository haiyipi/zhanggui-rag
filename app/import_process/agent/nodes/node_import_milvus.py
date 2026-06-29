"""
Milvus入库节点
将向量化后的切片数据存入 Milvus 数据库
"""
import sys
import json
from pathlib import Path
from typing import List, Dict, Any

from pymilvus import MilvusClient, DataType

from app.core.logger import logger
from app.import_process.agent.state import ImportGraphState
from app.utils.task_utils import add_running_task, add_done_task
from app.conf.milvus_config import milvus_config


def node_import_milvus(state: ImportGraphState) -> ImportGraphState:
    """
    Milvus入库节点

    核心流程：
        1. 获取切片数据
        2. 连接Milvus
        3. 清理旧数据（幂等性）
        4. 批量插入新数据
    """
    func_name = sys._getframe().f_code.co_name
    logger.info(f">>> 开始执行节点: {func_name}")

    add_running_task(state.get("task_id", ""), func_name)

    try:
        # 步骤1：获取切片数据
        chunks = state.get("chunks", [])
        if not chunks:
            logger.warning("无切片数据，跳过入库")
            return state

        item_name = state.get("item_name", "unknown")
        logger.info(f"开始入库，商品: {item_name}, 切片数: {len(chunks)}")

        # 步骤2：连接Milvus
        client = MilvusClient(uri=milvus_config.milvus_url)
        collection_name = milvus_config.chunks_collection

        # 步骤3：检查并创建集合
        if not _collection_exists(client, collection_name):
            _create_collection(client, collection_name)

        # 步骤4：清理旧数据
        _clean_old_data(client, collection_name, item_name)

        # 步骤5：插入数据
        inserted_count = _insert_chunks(client, collection_name, chunks)
        logger.info(f"成功入库 {inserted_count} 条数据")

        # 步骤6：保存结果
        _save_import_result(state, chunks)

    except Exception as e:
        logger.error(f"Milvus入库失败: {e}", exc_info=True)

    finally:
        add_done_task(state.get("task_id", ""), func_name)
        logger.info(f">>> 节点执行完成: {func_name}")

    return state


def _collection_exists(client: MilvusClient, collection_name: str) -> bool:
    """检查集合是否存在"""
    try:
        collections = client.list_collections()
        return collection_name in collections
    except Exception as e:
        logger.warning(f"检查集合失败: {e}")
        return False


def _create_collection(client: MilvusClient, collection_name: str):
    """创建集合（包含向量索引）"""
    try:
        # 定义 schema
        schema = client.create_schema(auto_id=True, enable_dynamic_field=True)

        # 添加字段
        schema.add_field(field_name="chunk_id", datatype=DataType.INT64, is_primary=True, auto_id=True)
        schema.add_field(field_name="content", datatype=DataType.VARCHAR, max_length=65535)
        schema.add_field(field_name="title", datatype=DataType.VARCHAR, max_length=65535)
        schema.add_field(field_name="parent_title", datatype=DataType.VARCHAR, max_length=65535)
        schema.add_field(field_name="file_title", datatype=DataType.VARCHAR, max_length=65535)
        schema.add_field(field_name="item_name", datatype=DataType.VARCHAR, max_length=65535)
        schema.add_field(field_name="dense_vector", datatype=DataType.FLOAT_VECTOR, dim=1024)
        schema.add_field(field_name="sparse_vector", datatype=DataType.SPARSE_FLOAT_VECTOR)

        # 创建索引参数
        index_params = client.prepare_index_params()

        # 稠密向量索引（HNSW 更快）
        index_params.add_index(
            field_name="dense_vector",
            index_name="dense_index",
            index_type="HNSW",
            metric_type="COSINE",
            params={"M": 16, "efConstruction": 200}
        )

        # 稀疏向量索引（必需！）
        index_params.add_index(
            field_name="sparse_vector",
            index_name="sparse_index",
            index_type="SPARSE_INVERTED_INDEX",
            metric_type="IP",
            params={"inverted_index_algo": "DAAT_MAXSCORE"}
        )

        # 创建集合
        client.create_collection(
            collection_name=collection_name,
            schema=schema,
            index_params=index_params
        )
        logger.info(f"集合 {collection_name} 创建成功")

    except Exception as e:
        logger.error(f"创建集合失败: {e}")
        raise


def _clean_old_data(client: MilvusClient, collection_name: str, item_name: str):
    """清理旧数据（幂等性）"""
    try:
        # 检查集合是否存在
        if collection_name not in client.list_collections():
            return

        # 删除指定商品的数据
        client.delete(
            collection_name=collection_name,
            filter=f'item_name == "{item_name}"'
        )
        logger.info(f"已清理商品 {item_name} 的旧数据")
    except Exception as e:
        logger.warning(f"清理旧数据失败: {e}")


def _insert_chunks(client: MilvusClient, collection_name: str, chunks: List[Dict]) -> int:
    """插入切片数据"""
    try:
        # 准备数据
        data = []
        for chunk in chunks:
            doc = {
                "content": chunk.get("content", ""),
                "title": chunk.get("title", ""),
                "parent_title": chunk.get("parent_title", ""),
                "file_title": chunk.get("file_title", ""),
                "item_name": chunk.get("item_name", ""),
                "dense_vector": chunk.get("dense_vector", []),
                "sparse_vector": chunk.get("sparse_vector", {})
            }
            data.append(doc)

        # 批量插入
        result = client.insert(
            collection_name=collection_name,
            data=data
        )
        return result.get("insert_count", 0)

    except Exception as e:
        logger.error(f"插入数据失败: {e}")
        return 0


def _save_import_result(state: ImportGraphState, chunks: List[Dict]):
    """保存入库结果到本地文件"""
    local_dir = state.get("local_dir", "")
    if not local_dir:
        return

    result_path = Path(local_dir) / "import_result.json"
    try:
        result = {
            "task_id": state.get("task_id"),
            "file_title": state.get("file_title"),
            "item_name": state.get("item_name"),
            "chunk_count": len(chunks),
            "chunks": chunks
        }
        with open(result_path, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        logger.info(f"入库结果已保存: {result_path}")
    except Exception as e:
        logger.warning(f"保存入库结果失败: {e}")


# ==================== 测试代码 ====================
if __name__ == "__main__":
    print("=" * 50)
    print("node_import_milvus 模块")
    print("=" * 50)