"""
检索流程主图
串联所有检索节点，形成完整的RAG问答流程
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from dotenv import load_dotenv
from langgraph.graph import StateGraph, END

from app.core.logger import logger
from app.query_process.agent.state import QueryGraphState
from app.query_process.agent.nodes.node_item_name_confirm import node_item_name_confirm
from app.query_process.agent.nodes.node_search_embedding import node_search_embedding
from app.query_process.agent.nodes.node_search_embedding_hyde import node_search_embedding_hyde
from app.query_process.agent.nodes.node_web_search_mcp import node_web_search_mcp
from app.query_process.agent.nodes.node_rrf import node_rrf
from app.query_process.agent.nodes.node_rerank import node_rerank
from app.query_process.agent.nodes.node_answer_output import node_answer_output

load_dotenv()


def create_query_graph():
    """
    创建检索流程图

    流程：
        START → node_item_name_confirm
                    ↓
            ┌───────┴───────┐
            ↓               ↓
        (有答案)        (无答案)
            ↓               ↓
        node_answer    node_multi_search
            ↓               ↓
            END              ↓
                    node_search_embedding
                            ↓
                    node_search_embedding_hyde
                            ↓
                    node_web_search_mcp
                            ↓
                    node_join (合并)
                            ↓
                    node_rrf (融合)
                            ↓
                    node_rerank (重排)
                            ↓
                    node_answer_output
                            ↓
                           END
    """
    logger.info("创建检索流程图")

    workflow = StateGraph(QueryGraphState)

    # 注册所有检索节点
    workflow.add_node("node_item_name_confirm", node_item_name_confirm)
    workflow.add_node("node_search_embedding", node_search_embedding)
    workflow.add_node("node_search_embedding_hyde", node_search_embedding_hyde)
    workflow.add_node("node_web_search_mcp", node_web_search_mcp)
    workflow.add_node("node_rrf", node_rrf)
    workflow.add_node("node_rerank", node_rerank)
    workflow.add_node("node_answer_output", node_answer_output)

    # 辅助节点（用于分支和合并）
    workflow.add_node("node_multi_search", lambda x: x)   # 多路检索分叉点
    workflow.add_node("node_join", lambda x: x)           # 多路检索合并点

    # 设置入口
    workflow.set_entry_point("node_item_name_confirm")

    # 条件路由
    def route_after_confirm(state: QueryGraphState) -> str:
        if state.get("answer"):
            return "node_answer_output"
        return "node_multi_search"

    workflow.add_conditional_edges(
        "node_item_name_confirm",
        route_after_confirm,
        {
            "node_multi_search": "node_multi_search",
            "node_answer_output": "node_answer_output"
        }
    )

    # 多路检索顺序执行（避免并发冲突）
    workflow.add_edge("node_multi_search", "node_search_embedding")
    workflow.add_edge("node_search_embedding", "node_search_embedding_hyde")
    workflow.add_edge("node_search_embedding_hyde", "node_web_search_mcp")
    workflow.add_edge("node_web_search_mcp", "node_join")

    # 后续流程
    workflow.add_edge("node_join", "node_rrf")
    workflow.add_edge("node_rrf", "node_rerank")
    workflow.add_edge("node_rerank", "node_answer_output")
    workflow.add_edge("node_answer_output", END)

    app = workflow.compile()
    logger.info("检索流程图创建成功")

    return app


# 全局应用实例
query_app = create_query_graph()


if __name__ == "__main__":
    print("=" * 50)
    print("检索流程图已创建")
    print("节点顺序:")
    print("  node_item_name_confirm")
    print("      ↓")
    print("  node_multi_search")
    print("      ↓")
    print("  node_search_embedding")
    print("      ↓")
    print("  node_search_embedding_hyde")
    print("      ↓")
    print("  node_web_search_mcp")
    print("      ↓")
    print("  node_join")
    print("      ↓")
    print("  node_rrf → node_rerank → node_answer_output")
    print("=" * 50)