"""
test_decorators.py
"""
import pytest

from core.addons.celery import celery
from core.task.decorators import queue_task


def test_queue_task_raises_exception_for_func():
    def test_sum():
        return 1 + 1

    with pytest.raises(Exception) as error:
        queue_task(test_sum)


def test_queue_task_returns_task_id():
    @celery.task()
    def test_sum():
        return 1 + 1

    task = queue_task(test_sum)

    assert task.id is not False
