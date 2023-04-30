"""
data.py
"""
from fastapi import APIRouter
from controller.misc.celery import celery
from controller.misc.dependencies import RequireAPIAuth

router = APIRouter(prefix="/api/data", tags=["data"])


@router.get("/task/{task_id}")
async def task_result(auth: RequireAPIAuth, task_id: str) -> dict:
    task = celery.AsyncResult(task_id)
    return {"status": task.status, "result": task.result}
