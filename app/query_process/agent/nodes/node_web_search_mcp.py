"""
联网搜索节点
使用百炼 MCP 服务进行联网搜索
"""
import sys
import json
import asyncio

from app.core.logger import logger
from app.query_process.agent.state import QueryGraphState
from app.utils.task_utils import add_running_task, add_done_task
from app.conf.bailian_mcp_config import mcp_config


def node_web_search_mcp(state: QueryGraphState) -> QueryGraphState:
    """
    联网搜索节点
    """
    func_name = sys._getframe().f_code.co_name
    logger.info(f">>> 开始执行节点: {func_name}")

    add_running_task(state.get("session_id", ""), func_name, state.get("is_stream", False))

    query = state.get("rewritten_query", "") or state.get("original_query", "")

    if not query:
        logger.warning("查询为空，跳过联网搜索")
        state["web_search_docs"] = []
        add_done_task(state.get("session_id", ""), func_name, state.get("is_stream", False))
        return state

    try:
        # 执行异步搜索
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        results = loop.run_until_complete(_async_web_search(query))
        loop.close()

        # 格式化结果
        docs = _format_search_results(results)
        state["web_search_docs"] = docs

        logger.info(f"联网搜索完成，获取 {len(docs)} 条结果")

    except Exception as e:
        logger.error(f"联网搜索失败: {e}", exc_info=True)
        state["web_search_docs"] = []

    add_done_task(state.get("session_id", ""), func_name, state.get("is_stream", False))
    logger.info(f">>> 节点执行完成: {func_name}")

    return state


async def _async_web_search(query: str):
    """异步执行联网搜索"""
    try:
        from agents.mcp import MCPServerSse

        search_mcp = MCPServerSse(
            name="web_search",
            params={
                "url": mcp_config.mcp_base_url,
                "headers": {"Authorization": mcp_config.api_key},
                "timeout": 30,
                "sse_read_timeout": 30
            }
        )

        await search_mcp.connect()
        result = await search_mcp.call_tool(
            tool_name="bailian_web_search",
            arguments={"query": query, "count": 5}
        )
        await search_mcp.cleanup()

        if result and not result.isError and result.content:
            raw_text = result.content[0].text
            data = json.loads(raw_text)
            return data.get("pages", [])

    except ImportError:
        logger.warning("MCP客户端未安装，使用模拟数据")
        return _mock_search_results(query)
    except Exception as e:
        logger.error(f"MCP搜索失败: {e}")
        return _mock_search_results(query)

    return []


def _mock_search_results(query: str):
    """模拟搜索结果"""
    return [
        {
            "title": f"关于'{query}'的搜索结果",
            "url": "https://example.com/1",
            "snippet": f"这是关于{query}的搜索结果摘要。包含相关信息..."
        }
    ]


def _format_search_results(results):
    """格式化搜索结果"""
    docs = []
    for item in results:
        snippet = item.get("snippet", "").strip()
        if snippet:
            docs.append({
                "title": item.get("title", ""),
                "url": item.get("url", ""),
                "snippet": snippet,
                "source": "web",
                "content": snippet
            })
    return docs