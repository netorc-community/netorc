"""
exceptions.py
"""


class APIError(Exception):
    def __init__(
            self,
            status_code: int,
            code: str,
            reason: str,
            message: str = None,
            reference_error: str = None,
    ):
        self.status_code = status_code
        self.code = code
        self.reason = reason
        self.message = message
        self.reference_error = reference_error


class TaskLockAddError(Exception):
    def __init__(self):
        self.message = (
            "Unable to add lock to task. A task using the same key is running."
        )
        super().__init__(self.message)
