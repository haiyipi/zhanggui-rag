"""
入口节点 - 文件类型判断与路由
负责接收外部输入的文件，识别文件类型，并根据类型开启相应的处理分支
"""
import os
import sys
from os.path import splitext
from pathlib import Path

from app.core.logger import logger
from app.import_process.agent.state import ImportGraphState, create_default_state
from app.utils.task_utils import add_running_task, add_done_task


def node_entry(state: ImportGraphState) -> ImportGraphState:
    """
    LangGraph知识库导入工作流 - 入口节点

    核心职责：
        1. 初始化参数校验
        2. 自动判断文件类型(PDF/MD)
        3. 设置解析开关
        4. 提取业务标识(file_title)

    Args:
        state: 导入流程状态，必须包含 local_file_path、task_id

    Returns:
        更新后的状态，新增 is_pdf_read_enabled/is_md_read_enabled/pdf_path/md_path/file_title
    """
    # 动态获取函数名
    func_name = sys._getframe().f_code.co_name
    logger.info(f">>> 开始执行节点: {func_name}")

    # 记录任务开始
    add_running_task(state.get("task_id", ""), func_name)

    # ==================== 1. 核心参数提取与非空校验 ====================
    document_path = state.get("local_file_path", "")
    if not document_path:
        logger.error(f"【{func_name}】核心参数缺失：local_file_path 为空")
        return state

    logger.info(f"【{func_name}】收到文件路径: {document_path}")

    # ==================== 2. 根据文件后缀判断类型 ====================
    file_ext = os.path.splitext(document_path)[1].lower()

    if file_ext == ".pdf":
        logger.info(f"【{func_name}】文件类型: PDF，开启PDF解析流程")
        state["is_pdf_read_enabled"] = True
        state["pdf_path"] = document_path

    elif file_ext == ".md":
        logger.info(f"【{func_name}】文件类型: Markdown，开启MD解析流程")
        state["is_md_read_enabled"] = True
        state["md_path"] = document_path

    else:
        logger.warning(f"【{func_name}】不支持的文件类型: {file_ext}，仅支持 .pdf 和 .md")
        # 不设置任何开关，流程将直接结束

    # ==================== 3. 提取文件标题 ====================
    file_name = os.path.basename(document_path)
    state["file_title"] = splitext(file_name)[0]
    logger.info(f"【{func_name}】文件标题: {state['file_title']}")

    # ==================== 4. 确保输出目录存在 ====================
    local_dir = state.get("local_dir", "")
    if local_dir:
        Path(local_dir).mkdir(parents=True, exist_ok=True)
        logger.info(f"【{func_name}】输出目录: {local_dir}")

    # 记录任务完成
    add_done_task(state.get("task_id", ""), func_name)
    logger.info(f">>> 节点执行完成: {func_name}")

    return state


# ==================== 测试代码 ====================
if __name__ == "__main__":
    from app.utils.path_util import PROJECT_ROOT

    print("\n" + "=" * 50)
    print("测试 node_entry 节点")
    print("=" * 50)

    # 测试1: PDF文件
    print("\n📄 测试1: PDF文件")
    test_state_pdf = create_default_state(
        task_id="test_pdf_001",
        local_file_path=str(PROJECT_ROOT / "doc" / "hak180产品安全手册.pdf"),
        local_dir=str(PROJECT_ROOT / "output")
    )
    result = node_entry(test_state_pdf)
    print(f"   is_pdf_read_enabled: {result.get('is_pdf_read_enabled')}")
    print(f"   file_title: {result.get('file_title')}")

    # 测试2: MD文件
    print("\n📝 测试2: MD文件")
    test_state_md = create_default_state(
        task_id="test_md_001",
        local_file_path=str(PROJECT_ROOT / "doc" / "example.md"),
        local_dir=str(PROJECT_ROOT / "output")
    )
    result = node_entry(test_state_md)
    print(f"   is_md_read_enabled: {result.get('is_md_read_enabled')}")
    print(f"   file_title: {result.get('file_title')}")

    # 测试3: 不支持的文件
    print("\n❌ 测试3: 不支持的文件类型")
    test_state_txt = create_default_state(
        task_id="test_txt_001",
        local_file_path=str(PROJECT_ROOT / "doc" / "example.txt"),
        local_dir=str(PROJECT_ROOT / "output")
    )
    result = node_entry(test_state_txt)
    print(f"   is_pdf_read_enabled: {result.get('is_pdf_read_enabled')}")
    print(f"   is_md_read_enabled: {result.get('is_md_read_enabled')}")

    print("\n" + "=" * 50)
    print("✅ 节点测试完成")