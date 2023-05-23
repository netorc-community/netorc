from passlib.hash import pbkdf2_sha256

from core import db
from core.db.tables import User
from core.metrics.logging import logger


def create_user(user: User, session=next(db.get_session())):
    """
    Creates a new database user based on User object.
    Hashes user password and api key using SHA256.

    Args:
        user: User object
        session: database session

    Returns:
        bool: True
    """
    user.password = pbkdf2_sha256.hash(user.password)
    user.api_key = pbkdf2_sha256.hash(user.api_key)

    try:
        session.add(user)
        session.commit()

    except Exception as exc:
        logger.error("Error creating superuser")
        raise

    logger.info("User: %s, created", user.username)
    return True
