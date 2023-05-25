from typing import Callable

from passlib.hash import pbkdf2_sha256

from core import db
from core.db.tables import User
from core.metrics.logging import logger


def create_user(user: User, session: Callable = db.get_session):
    """
    Creates a new database user based on User object.
    Hashes user password and api key using SHA256.

    Args:
        user: User object
        session: database session

    Returns:
        user: database user object
    """
    user.password = pbkdf2_sha256.hash(user.password)
    user.api_key = pbkdf2_sha256.hash(user.api_key)

    with session() as _session:
        _session.add(user)
        _session.commit()
        logger.info("User: %s, created", user.username)
        return user
