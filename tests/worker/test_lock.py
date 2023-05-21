from core.task.decorators import lock_task


def test_lock_task():
    @lock_task
    def example():
        return True

    assert example(task_lock_key="netorc_test")
    assert example()
