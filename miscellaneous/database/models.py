"""
models.py
"""
from datetime import datetime
from typing import Optional
from sqlmodel import Field, SQLModel

class UserModel(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    firstname: Optional[str]
    lastname: Optional[str]
    email: str
    username: str
    password: str
    password_salt: str
    api_key: str
    api_key_salt: str
    created: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    last_updated: datetime = Field(default_factory=datetime.utcnow, nullable=False)

