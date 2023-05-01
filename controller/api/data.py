"""
data.py
"""
from fastapi import APIRouter
from controller.misc.celery import celery

router = APIRouter(prefix="/api/data", tags=["data"])


@router.get("/task/{task_id}")
async def task_result(task_id: str) -> list:
    task = celery.AsyncResult(task_id)
    return [{"status": task.status, "result": task.result}]
