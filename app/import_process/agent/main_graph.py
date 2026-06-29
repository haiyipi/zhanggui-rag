"""
导入流程主图
串联所有导入节点，形成完整的知识库导入流水线
"""
import sys
import os
from pathlib import Path

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from dotenv import load_dotenv
from langgraph.graph import StateGraph, END

from app.core.logger import logger
from app.import_process.agent.state import ImportGraphState, create_default_state
from app.import_process.agent.nodes.node_entry import node_entry
from app.import_process.agent.nodes.node_pdf_to_md import node_pdf_to_md
from app.import_process.agent.nodes.node_md_img import node_md_img
from app.import_process.agent.nodes.node_document_split import node_document_split
from app.import_process.agent.nodes.node_item_name_recognition import node_item_name_recognition
from app.import_process.agent.nodes.node_bge_embedding import node_bge_embedding
from app.import_process.agent.nodes.node_import_milvus import node_import_milvus

load_dotenv()


def create_import_graph():
    """创建导入流程图"""
    logger.info("创建导入流程图")

    workflow = StateGraph(ImportGraphState)

    # 注册导入流程节点
    workflow.add_node("node_entry", node_entry)
    workflow.add_node("node_pdf_to_md", node_pdf_to_md)
    workflow.add_node("node_md_img", node_md_img)
    workflow.add_node("node_document_split", node_document_split)
    workflow.add_node("node_item_name_recognition", node_item_name_recognition)
    workflow.add_node("node_bge_embedding", node_bge_embedding)
    workflow.add_node("node_import_milvus", node_import_milvus)

    # 设置入口
    workflow.set_entry_point("node_entry")

    # 条件路由
    def route_after_entry(state: ImportGraphState) -> str:
        if state.get("is_pdf_read_enabled"):
            return "node_pdf_to_md"
        elif state.get("is_md_read_enabled"):
            return "node_md_img"
        else:
            return END

    workflow.add_conditional_edges(
        "node_entry",
        route_after_entry,
        {
            "node_pdf_to_md": "node_pdf_to_md",
            "node_md_img": "node_md_img",
            END: END
        }
    )

    # 顺序边
    workflow.add_edge("node_pdf_to_md", "node_md_img")
    workflow.add_edge("node_md_img", "node_document_split")
    workflow.add_edge("node_document_split", "node_item_name_recognition")
    workflow.add_edge("node_item_name_recognition", "node_bge_embedding")
    workflow.add_edge("node_bge_embedding", "node_import_milvus")
    workflow.add_edge("node_import_milvus", END)

    app = workflow.compile()
    logger.info("导入流程图创建成功")

    return app


kb_import_app = create_import_graph()


if __name__ == "__main__":
    print("导入流程已创建")