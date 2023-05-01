"""
task.py
"""
from fastapi import APIRouter
from controller.misc.celery import celery

router = APIRouter(prefix="/api/task", tags=["task"])


@router.get("/{task_id}")
async def task(task_id: str, cancel: bool = False) -> list:
    _task = celery.control
    if cancel is True:
        _task.revoke(task_id, terminate=True)
        return [{"revoked": task_id}]
    _query = _task.inspect().query_task(task_id)
    return [_query]
