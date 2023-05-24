"""
models.py
"""
from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel


class UserCreate(SQLModel):
    firstname: Optional[str]
    lastname: Optional[str]
    email: Optional[str]
    username: str
    password: str
    api_key: str


class UserRead(SQLModel):
    firstname: Optional[str]
    lastname: Optional[str]
    email: Optional[str]
    username: str
    created: datetime
    last_updated: datetime
