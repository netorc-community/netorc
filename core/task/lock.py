"""
task_lock.py
"""
import time
import uuid

import redis

from core.addons.exceptions import AddLockException
from core.metrics.logging import logger
from settings import settings


class TaskLock:
    """Distributed lock mechanism to Add/Remove lock on a task"""

    def __init__(self, task_lock_key: str = None, timeout: int = 30):
        try:
            self.conn = redis.from_url(settings.redis)
            logger.info("Connected to redis instance: %s", settings.redis)
        except Exception as exc:
            logger.critical(
                "An exception occurred connecting to redis instance: %s",
                settings.redis,
            )
            raise exc

        self.task_lock_key = "lock:" + task_lock_key
        self.uid = str(uuid.uuid4())
        self.timeout = timeout

    def add(self):
        """Add the lock

        :returns: True
        """
        end = time.time() + self.timeout
        while time.time() < end:
            try:
                if self.conn.setnx(self.task_lock_key, self.uid):
                    logger.info("Added %s with uid: %s", self.task_lock_key, self.uid)
                    return True
                time.sleep(0.01)
            except Exception as exc:
                logger.error(
                    "An exception occurred adding %s with uid %s",
                    self.task_lock_key,
                    self.uid,
                )
                raise exc
        raise AddLockException

    def remove(self):
        """Remove the lock

        :returns: True
        """

        pipe = self.conn.pipeline(True)
        while True:
            try:
                pipe.watch(self.task_lock_key)
                if self.conn.get(self.task_lock_key).decode("utf-8") == self.uid:
                    pipe.multi()
                    pipe.delete(self.task_lock_key)
                    pipe.execute()
                    logger.info("Removed %s with uid: %s", self.task_lock_key, self.uid)
                    return True
                pipe.unwatch()
                break
            except redis.exceptions.WatchError as exc:
                logger.critical(
                    "Key changed during transaction, failed to remove %s with uid: %s",
                    self.task_lock_key,
                    self.uid,
                )
                raise exc
