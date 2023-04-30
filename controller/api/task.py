"""
task.py
"""
from fastapi import APIRouter
from controller.misc.celery import celery
from controller.misc.dependencies import RequireAPIAuth

router = APIRouter(prefix="/api/task", tags=["task"])


@router.get("/{task_id}")
async def task(auth: RequireAPIAuth, task_id: str, cancel: bool = False) -> dict:
    _task = celery.control
    if cancel is True:
        _task.revoke(task_id, terminate=True)
        return {"revoked": task_id}
    _query = _task.inspect().query_task(task_id)
    return _query
