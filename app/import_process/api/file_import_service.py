"""
文件导入 Web 服务
提供文件上传、任务状态查询、静态页面服务
"""
import os
import sys
import uuid
import shutil
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))

from fastapi import FastAPI, UploadFile, File, BackgroundTasks, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse, JSONResponse
import uvicorn

from app.core.logger import logger
from app.utils.path_util import PROJECT_ROOT
from app.utils.task_utils import (
    add_running_task,
    add_done_task,
    get_done_task_list,
    get_running_task_list,
    update_task_status,
    get_task_status,
    TASK_STATUS_PENDING,
    TASK_STATUS_PROCESSING,
    TASK_STATUS_COMPLETED,
    TASK_STATUS_FAILED,
)
from app.import_process.agent.state import create_default_state
from app.import_process.agent.main_graph import kb_import_app
from app.clients.minio_utils import get_minio_client

# ==================== 初始化 FastAPI ====================
app = FastAPI(
    title="File Import Service",
    description="知识库文件导入服务 - 支持 PDF/MD 文件上传和自动处理",
    version="1.0.0"
)

# 配置 CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ==================== 静态页面 ====================
@app.get("/import.html", response_class=HTMLResponse)
async def get_import_page():
    """返回文件导入前端页面"""
    from app.utils.path_util import PROJECT_ROOT

    html_path = PROJECT_ROOT / "app" / "import_process" / "page" / "import.html"

    if not html_path.exists():
        return HTMLResponse(content="<h1>404 - import.html not found</h1>", status_code=404)

    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()

    return HTMLResponse(content=html_content)


# ==================== 健康检查 ====================
@app.get("/health")
async def health_check():
    """健康检查接口"""
    return {"status": "ok", "service": "file_import_service"}


# ==================== 后台任务 ====================
def run_import_task(task_id: str, local_dir: str, local_file_path: str):
    """后台执行导入任务"""
    try:
        update_task_status(task_id, TASK_STATUS_PROCESSING)
        logger.info(f"[{task_id}] 开始执行导入任务: {local_file_path}")

        init_state = create_default_state(
            task_id=task_id,
            local_dir=local_dir,
            local_file_path=local_file_path,
            is_stream=False
        )

        final_state = kb_import_app.invoke(init_state)

        update_task_status(task_id, TASK_STATUS_COMPLETED)

        chunks_count = len(final_state.get("chunks", []))
        item_name = final_state.get("item_name", "")
        logger.info(f"[{task_id}] 导入任务完成: 商品={item_name}, 切片数={chunks_count}")

    except Exception as e:
        logger.error(f"[{task_id}] 导入任务失败: {e}", exc_info=True)
        update_task_status(task_id, TASK_STATUS_FAILED)


# ==================== 文件上传接口 ====================
@app.post("/upload")
async def upload_files(
        background_tasks: BackgroundTasks,
        files: List[UploadFile] = File(..., description="要上传的文件（支持PDF/MD）")
):
    """上传文件接口"""
    date_str = datetime.now().strftime("%Y%m%d")
    base_output_dir = PROJECT_ROOT / "output" / date_str
    base_output_dir.mkdir(parents=True, exist_ok=True)

    results = []

    for file in files:
        file_ext = os.path.splitext(file.filename)[1].lower()
        if file_ext not in [".pdf", ".md"]:
            results.append({"filename": file.filename, "success": False, "error": f"不支持的文件类型: {file_ext}"})
            continue

        task_id = str(uuid.uuid4())
        task_dir = base_output_dir / task_id
        task_dir.mkdir(parents=True, exist_ok=True)

        file_path = task_dir / file.filename
        try:
            with open(file_path, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            logger.info(f"[{task_id}] 文件保存成功: {file_path}")
        except Exception as e:
            logger.error(f"[{task_id}] 文件保存失败: {e}")
            results.append({"filename": file.filename, "success": False, "error": f"文件保存失败: {str(e)}"})
            continue

        # 上传到 MinIO
        try:
            minio_client = get_minio_client()
            if minio_client:
                bucket = os.getenv("MINIO_BUCKET_NAME", "knowledge-base-files")
                object_name = f"uploads/{date_str}/{task_id}/{file.filename}"
                minio_client.fput_object(bucket, object_name, str(file_path))
                logger.info(f"[{task_id}] 文件已上传到 MinIO: {object_name}")
        except Exception as e:
            logger.warning(f"[{task_id}] MinIO 上传失败: {e}")

        background_tasks.add_task(run_import_task, task_id, str(task_dir), str(file_path))

        results.append(
            {"filename": file.filename, "success": True, "task_id": task_id, "message": "文件已接收，正在处理中"})

    return JSONResponse(content={"code": 200, "message": f"收到 {len(files)} 个文件", "results": results})


# ==================== 任务状态查询 ====================
@app.get("/status/{task_id}")
async def get_task_status_info(task_id: str):
    """查询任务状态"""
    status = get_task_status(task_id)
    if not status:
        raise HTTPException(status_code=404, detail=f"任务 {task_id} 不存在")

    return {
        "code": 200,
        "task_id": task_id,
        "status": status,
        "done_list": get_done_task_list(task_id),
        "running_list": get_running_task_list(task_id)
    }


# ==================== 任务列表 ====================
@app.get("/tasks")
async def list_tasks():
    """列出所有任务"""
    return {"code": 200, "message": "任务列表功能待实现", "tasks": []}


# ==================== 启动入口 ====================
if __name__ == "__main__":
    logger.info("启动文件导入服务...")
    uvicorn.run(app, host="127.0.0.1", port=8002)