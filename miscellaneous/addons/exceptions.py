class AddLockException(Exception):
    """Exception raised for lock not aquired"""

    def __init__(self):
        self.message = (
            "Unable to add lock to task. A task using the same key is running."
        )
        super().__init__(self.message)
