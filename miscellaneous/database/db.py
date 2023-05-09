"""
db.py
"""
from sqlmodel import create_engine
from settings import settings


engine = create_engine(settings.database, echo=True)
