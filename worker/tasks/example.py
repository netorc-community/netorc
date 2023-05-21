"""
example.py

`lock_task` can be used to ensure tasks are executed
synchronously with each worker obtaining the lock before 
executing the task. 

for more information, see <link>

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
