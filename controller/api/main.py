"""
main.py
"""
from fastapi import FastAPI
from controller.misc.decorators import queue_task
from controller.worker.tasks.example import example_task
from controller.api import data
from controller.api import task
from controller.api import metrics

fastapi = FastAPI()
fastapi.include_router(data.router)
fastapi.include_router(task.router)
fastapi.include_router(metrics.router)


@fastapi.get("/api")
async def example() -> list:
    task = queue_task(example_task)
    return [{"id": task.id}]
