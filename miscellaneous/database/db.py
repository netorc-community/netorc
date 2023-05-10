"""
db.py
"""
from sqlmodel import create_engine, Session
from settings import settings


engine = create_engine(settings.database, echo=True)


def get_session():
    with Session(engine) as session:
        yield session
