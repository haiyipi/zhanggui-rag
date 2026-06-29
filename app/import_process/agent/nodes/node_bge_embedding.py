"""
BGE向量化节点
将文本切片转换为稠密+稀疏向量
"""
import os
import sys
from typing import List, Dict, Any

from app.core.logger import logger
from app.import_process.agent.state import ImportGraphState
from app.utils.task_utils import add_running_task, add_done_task


def node_bge_embedding(state: ImportGraphState) -> ImportGraphState:
    """
    BGE向量化节点

    核心流程：
        1. 获取切片数据
        2. 生成向量（稠密+稀疏）
        3. 更新状态

    Args:
        state: 导入流程状态

    Returns:
        更新后的状态，chunks 新增 dense_vector 和 sparse_vector
    """
    func_name = sys._getframe().f_code.co_name
    logger.info(f">>> 开始执行节点: {func_name}")

    add_running_task(state.get("task_id", ""), func_name)

    try:
        # 步骤1：获取切片
        chunks = state.get("chunks", [])
        if not chunks:
            logger.warning("无切片数据，跳过向量化")
            return state

        logger.info(f"开始向量化，共 {len(chunks)} 个切片")

        # 步骤2：生成向量
        chunks = step_generate_embeddings(chunks)

        # 步骤3：更新状态
        state["chunks"] = chunks
        state["embeddings_content"] = chunks

        logger.info(f"向量化完成，共 {len(chunks)} 个切片")

    except Exception as e:
        logger.error(f"向量化失败: {e}", exc_info=True)

    finally:
        add_done_task(state.get("task_id", ""), func_name)
        logger.info(f">>> 节点执行完成: {func_name}")

    return state


def step_generate_embeddings(chunks: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    """
    生成向量（简化版 - 模拟向量）

    注意：完整版需要调用 BGE-M3 模型生成真实向量
    当前使用模拟向量便于测试流程
    """
    import random

    for i, chunk in enumerate(chunks):
        content = chunk.get("content", "")
        item_name = chunk.get("item_name", "")

        # 构建输入文本
        text = f"{item_name}\n{content}" if item_name else content

        # 模拟稠密向量（1024维）
        dense_vector = [random.uniform(-0.1, 0.1) for _ in range(1024)]

        # 模拟稀疏向量
        sparse_vector = {1: 0.5, 2: 0.3, 3: 0.2}

        chunk["dense_vector"] = dense_vector
        chunk["sparse_vector"] = sparse_vector
        chunk["embedding_text"] = text

        logger.debug(f"Chunk {i + 1} 向量生成完成")

    return chunks


# ==================== 测试代码 ====================
if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("测试 node_bge_embedding 节点")
    print("=" * 50)

    # 创建测试切片
    test_chunks = [
        {
            "title": "# HAK 180 烫金机使用手册",
            "content": "HAK 180 烫金机是一款高性能烫金设备。",
            "item_name": "HAK 180 烫金机",
            "file_title": "hak180产品安全手册"
        }
    ]

    test_state = {
        "task_id": "test_bge_001",
        "chunks": test_chunks,
        "is_stream": False
    }

    try:
        result = node_bge_embedding(test_state)
        chunks = result.get("chunks", [])

        print(f"\n✅ 测试完成")
        print(f"   切片数: {len(chunks)}")

        if chunks:
            first = chunks[0]
            has_dense = "dense_vector" in first
            has_sparse = "sparse_vector" in first
            print(f"   稠密向量: {'有' if has_dense else '无'}")
            print(f"   稀疏向量: {'有' if has_sparse else '无'}")

            if has_dense:
                print(f"   向量维度: {len(first['dense_vector'])}")

    except Exception as e:
        print(f"\n❌ 测试失败: {e}")
        import traceback

        traceback.print_exc()