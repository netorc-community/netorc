"""
tables.py
"""
from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    firstname: Optional[str]
    lastname: Optional[str]
    email: str
    username: str = Field(index=True)
    password: str
    api_key: str
    created: datetime = Field(default_factory=datetime.utcnow, nullable=False)
    last_updated: datetime = Field(default_factory=datetime.utcnow, nullable=False)


class Service(SQLModel, table=True):
    id: str = Field(primary_key=True)
    name: str = Field(index=True)
    description: str = Field(max_length=256, default=None)
    service_type: Optional[str] = Field(default=None, foreign_key="servicetype.name", nullable=True)
    service_resource: Optional[str] = Field(default=None)
    category: str  # Customer facing or resource facing services
    state: str = Field(index=True)  # States include, inactive, active and terminated
    start_date: datetime
    end_date: datetime = Field(default=None)
    href: str


class ServiceType(SQLModel, table=True):
    id: str = Field(primary_key=True)
    name: str = Field(index=True, unique=True)
    description: str = Field(max_length=256, default=None)
    version: Optional[int] = Field(default=None)  # Service specific version
    href: str
