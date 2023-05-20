from sqlmodel import create_engine, Session

from settings import settings

engine = create_engine(settings.database)


def get_session():
    with Session(engine) as session:
        yield session
