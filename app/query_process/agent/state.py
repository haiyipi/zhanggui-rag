"""
检索流程状态定义
所有检索节点共享的数据结构
"""
from typing import TypedDict, List, Dict, Any, Optional, Annotated
import operator


def merge_session_id(current: str, new: str) -> str:
    """当有并发更新时，直接使用最新的值"""
    return new if new else current


class QueryGraphState(TypedDict):
    """
    查询流程图的状态定义
    """

    # ==================== 基础标识 ====================
    session_id: Annotated[str, merge_session_id]  # 会话唯一标识（支持并发）
    original_query: str  # 用户原始问题

    # ==================== 意图识别 ====================
    item_names: List[str]  # 提取出的商品名称
    rewritten_query: str  # 改写后的问题
    history: List[Dict[str, Any]]  # 历史对话记录
    is_stream: bool  # 是否流式输出标记

    # ==================== 检索结果 ====================
    embedding_chunks: List[Dict[str, Any]]  # 普通向量检索回来的切片
    hyde_embedding_chunks: List[Dict[str, Any]]  # HyDE 检索回来的切片
    kg_chunks: List[Dict[str, Any]]  # 图谱检索回来的切片
    web_search_docs: List[Dict[str, Any]]  # 网络搜索回来的文档

    # ==================== 排序结果 ====================
    rrf_chunks: List[Dict[str, Any]]  # RRF 融合排序后的切片
    reranked_docs: List[Dict[str, Any]]  # 重排序后的最终 Top-K 文档

    # ==================== 生成结果 ====================
    prompt: str  # 组装好的 Prompt
    answer: str  # 最终生成的答案

    # 辅助字段
    tmp: Annotated[List, operator.add]  # 用于吸收并发更新


# ==================== 默认状态配置 ====================
def get_default_query_state() -> QueryGraphState:
    """获取默认的查询状态"""
    return {
        "session_id": "",
        "original_query": "",
        "item_names": [],
        "rewritten_query": "",
        "history": [],
        "is_stream": False,
        "embedding_chunks": [],
        "hyde_embedding_chunks": [],
        "kg_chunks": [],
        "web_search_docs": [],
        "rrf_chunks": [],
        "reranked_docs": [],
        "prompt": "",
        "answer": "",
        "tmp": []
    }


def create_default_query_state(**overrides) -> QueryGraphState:
    """创建默认查询状态，支持覆盖"""
    state = get_default_query_state()
    state.update(overrides)
    return state


# ==================== 测试代码 ====================
if __name__ == "__main__":
    print("=" * 50)
    print("测试检索流程状态定义")
    print("=" * 50)

    state = create_default_query_state(
        session_id="test_session_001",
        original_query="万用表怎么用？",
        is_stream=True
    )

    print(f"session_id: {state['session_id']}")
    print(f"original_query: {state['original_query']}")
    print(f"is_stream: {state['is_stream']}")

    print("\n✅ 检索状态定义测试通过")