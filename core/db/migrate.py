from sqlmodel import SQLModel

from core import db
from core.metrics.logging import logger


def migrate() -> bool:
    try:
        SQLModel.metadata.create_all(db.engine)
        logger.info("Successfully migrated tables to database")
        return True

    except Exception as exc:
        logger.error("Error migrating tables to database: %s", exc)
        raise
