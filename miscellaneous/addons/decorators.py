"""
decorators.py
"""
from functools import wraps
from miscellaneous.addons.task_lock import TaskLock
from miscellaneous.metrics.logging import logger
from miscellaneous.addons.exceptions import AddLockException


def task_lock(func):
    """Applied to tasks which require synchronous execution.
    Workers will acquire a lock on the task before execution.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        if "task_lock_key" in kwargs:
            task_lock_key = kwargs.get("task_lock_key")
            logger.debug(
                "Found task lock key for %s, using: %s as key",
                func.__name__,
                task_lock_key,
            )
            kwargs.pop("task_lock_key")
        else:
            task_lock_key = func.__name__
            logger.debug(
                "No task lock key found for %s, using: %s as key",
                func.__name__,
                task_lock_key,
            )

        try:
            try:
                lock = TaskLock(task_lock_key)

            except Exception as exc:
                raise exc

            lock.add()

        except AddLockException as exc:
            logger.error(
                "Unable to add lock for task: %s, with key: %s",
                func.__name__,
                task_lock_key,
            )
            raise exc

        try:
            return func(*args, **kwargs)

        except Exception as exc:
            logger.error("An exception occurred when executing: %s", func.__name__)
            raise exc

        finally:
            try:
                lock.remove()

            except Exception as exc:
                raise exc

    return wrapper


def queue_task(func, priority: int = 0, *args, **kwargs):
    """Applied to tasks. Allows the calling of a Celery task
    and its arguments to be abstracted.
    """

    def wrapper():
        try:
            getattr(func, "apply_async")

        except Exception as exc:
            logger.error(
                "Function %s is not a celery task, have you missed a decorator?",
                func.__name__,
            )
            raise exc

        try:
            task = func.apply_async(args=[*args], kwargs={**kwargs}, priority=priority)
            return task

        except Exception as exc:
            logger.error("An exception occurred when queuing: %s", func.__name__)
            raise exc

    return wrapper()
