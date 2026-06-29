"""
导入流程状态定义
所有导入节点共享的数据结构
"""
from typing import TypedDict, List, Dict, Any, Optional


class ImportGraphState(TypedDict):
    """
    导入流程图的状态定义，包含所有节点产生和消费的数据字段。
    TypedDict 让我们在代码中能有自动补全和类型检查。
    """

    # ==================== 基础标识 ====================
    task_id: str  # 任务唯一ID，用于追踪日志
    file_title: str  # 文件标题（文件名去后缀）

    # ==================== 路径相关 ====================
    local_dir: str  # 当前工作目录或输出目录
    local_file_path: str  # 原始输入文件路径
    pdf_path: str  # PDF 文件路径 (如果输入是PDF)
    md_path: str  # Markdown 文件路径 (转换后或直接输入的)

    # ==================== 流程控制标记 ====================
    is_md_read_enabled: bool  # 是否启用 Markdown 读取路径
    is_pdf_read_enabled: bool  # 是否启用 PDF 读取路径

    # ==================== 内容数据 ====================
    md_content: str  # Markdown 的全文内容
    chunks: List[Dict[str, Any]]  # 切片后的文本列表，包含 metadata
    item_name: str  # 识别出的主体名称 (如: "万用表")

    # ==================== 向量相关 ====================
    embeddings_content: List[Dict[str, Any]]  # 包含向量数据的列表，准备写入 Milvus


# ==================== 默认状态配置 ====================
def get_default_state() -> ImportGraphState:
    """
    获取默认状态，用于初始化
    """
    return {
        "task_id": "",
        "file_title": "",
        "local_dir": "",
        "local_file_path": "",
        "pdf_path": "",
        "md_path": "",
        "is_md_read_enabled": False,
        "is_pdf_read_enabled": False,
        "md_content": "",
        "chunks": [],
        "item_name": "",
        "embeddings_content": [],
    }


def create_default_state(**overrides) -> ImportGraphState:
    """
    创建默认状态，支持覆盖特定字段

    Args:
        **overrides: 要覆盖的字段（关键字参数）

    Returns:
        新的状态实例

    Examples:
        state = create_default_state(
            task_id="task_001",
            local_file_path="doc/test.pdf"
        )
    """
    state = get_default_state()
    state.update(overrides)
    return state


# ==================== 测试代码 ====================
if __name__ == "__main__":
    print("=" * 50)
    print("测试导入流程状态定义")
    print("=" * 50)

    # 测试创建默认状态
    state = get_default_state()
    print(f"默认状态: {state}")

    # 测试创建带参数的状态
    test_state = create_default_state(
        task_id="test_001",
        local_file_path="doc/hak180.pdf",
        is_pdf_read_enabled=True
    )
    print(f"\n测试状态:")
    print(f"  - task_id: {test_state['task_id']}")
    print(f"  - local_file_path: {test_state['local_file_path']}")
    print(f"  - is_pdf_read_enabled: {test_state['is_pdf_read_enabled']}")

    print("\n✅ 状态定义测试通过")