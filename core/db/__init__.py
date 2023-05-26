from contextlib import contextmanager

from sqlmodel import create_engine, Session

from settings import settings

engine = create_engine(settings.database)


def require_db_session():
    with Session(engine) as session:
        try:
            yield session
        except Exception:
            session.rollback()
            raise
        finally:
            session.close()


@contextmanager
def get_session():
    with Session(engine) as session:
        try:
            yield session

        except Exception:
            session.rollback()
            raise

        finally:
            session.close()
