"""
检索服务端 - 完整版
"""
import sys
import os
import uuid

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from fastapi import FastAPI, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import uvicorn

from app.core.logger import logger
from app.query_process.agent.main_graph import query_app
from app.query_process.agent.state import create_default_query_state
from app.clients.mongo_history_utils import save_chat_message


app = FastAPI(title="Query Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QueryRequest(BaseModel):
    query: str
    session_id: str | None = None
    is_stream: bool = False


@app.get("/chat.html", response_class=HTMLResponse)
async def get_chat_page():
    return HTMLResponse(content="""<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><title>掌柜智库</title>
<style>
body { font-family: Arial; max-width: 600px; margin: 50px auto; padding: 20px; }
.chat-container { border: 1px solid #ccc; border-radius: 10px; overflow: hidden; }
.messages { height: 400px; overflow-y: auto; padding: 10px; background: #f9f9f9; }
.user { text-align: right; margin: 10px 0; }
.user span { background: #007bff; color: white; padding: 8px 12px; border-radius: 15px; display: inline-block; }
.assistant { text-align: left; margin: 10px 0; }
.assistant span { background: #e9ecef; color: #333; padding: 8px 12px; border-radius: 15px; display: inline-block; }
.input-area { display: flex; padding: 10px; border-top: 1px solid #ccc; }
.input-area input { flex: 1; padding: 10px; border: 1px solid #ccc; border-radius: 5px; }
.input-area button { margin-left: 10px; padding: 10px 20px; background: #007bff; color: white; border: none; border-radius: 5px; cursor: pointer; }
h2 { text-align: center; }
</style>
</head>
<body>
<h2>📚 掌柜智库</h2>
<div class="chat-container">
<div class="messages" id="messages"></div>
<div class="input-area">
<input type="text" id="question" placeholder="输入问题..." onkeypress="if(event.keyCode==13) send()">
<button onclick="send()">发送</button>
</div>
</div>
<script>
const API_BASE = 'http://127.0.0.1:8001';
let sessionId = 'session_' + Date.now();
function addMessage(role, text) {
    const div = document.createElement('div');
    div.className = role;
    div.innerHTML = '<span>' + text + '</span>';
    document.getElementById('messages').appendChild(div);
}
async function send() {
    const input = document.getElementById('question');
    const q = input.value.trim();
    if (!q) return;
    input.value = '';
    addMessage('user', q);
    const res = await fetch(API_BASE + '/query', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({query: q, session_id: sessionId})
    });
    const data = await res.json();
    addMessage('assistant', data.answer);
}
addMessage('assistant', '您好！我是掌柜智库助手，请问有什么可以帮助您的？');
</script>
</body>
</html>""")


@app.post("/query")
async def query(background_tasks: BackgroundTasks, request: QueryRequest):
    session_id = request.session_id or str(uuid.uuid4())
    logger.info(f"[{session_id}] 收到查询: {request.query}")

    save_chat_message(session_id, "user", request.query, "", [])

    init_state = create_default_query_state(
        session_id=session_id,
        original_query=request.query,
        is_stream=False
    )

    final_state = query_app.invoke(init_state)
    answer = final_state.get("answer", "抱歉，无法生成答案")

    save_chat_message(session_id, "assistant", answer, "", final_state.get("item_names", []))

    return {"code": 200, "session_id": session_id, "answer": answer}


@app.get("/health")
async def health():
    return {"status": "ok"}


if __name__ == "__main__":
    print("启动查询服务... http://127.0.0.1:8001/chat.html")
    uvicorn.run(app, host="127.0.0.1", port=8001)