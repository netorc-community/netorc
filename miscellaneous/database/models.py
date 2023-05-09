"""
models.py
"""

from typing import Optional
from sqlmodel import SQLModel, Field


class UserCreate(SQLModel):
    firstname: Optional[str]
    lastname: Optional[str]
    email: str
    username: str = Field(index=True)
    password: str
    password_salt: str
    api_key: str
    api_key_salt: str


class UserRead(SQLModel):
    firstname: Optional[str]
    lastname: Optional[str]
    email: str
    username: str = Field(index=True)
