"""
main.py
"""
from fastapi import FastAPI
from worker_service.tasks.example import example_task
from miscellaneous.addons.decorators import queue_task


fastapi = FastAPI()


@fastapi.get("/api")
async def example() -> list:
    task = queue_task(example_task)
    return [{"id": task.id}]
