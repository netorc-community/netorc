"""
models.py
"""
from miscellaneous.database.db import Base


class User(Base):
    __tablename__ = "users"
