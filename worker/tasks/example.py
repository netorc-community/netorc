"""
example.py

`lock_task` can be used to ensure tasks are executed
synchronously with each worker obtaining the lock before 
executing the task. 

for more information, see <link>

@celery.task()
@lock_task
def a_locked_task() -> None:
    print("Starting a task with task_lock...")
    time.sleep(10)
    print("Finished task with task_lock.")


@celery.task()
@lock_task
def a_locked_task(task_lock_key: str = None) -> None:
    print(f"Starting task: {task_lock_key}, with task_lock...")
    time.sleep(10)
    print(f"Finished task: {task_lock_key}, with task_lock.")

"""
import time

from core.addons.celery import celery
from core.task.decorators import lock_task


@celery.task()
@lock_task
def example_task() -> None:
    print("Starting task")
    time.sleep(2)
    print("Finished task")
    return 8
