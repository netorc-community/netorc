"""
manage.py
"""
import sys

from sqlmodel import SQLModel
from core import db
from core.db import tables


def main():
    if "migrate" in sys.argv:
        SQLModel.metadata.create_all(db.engine)


if __name__ == "__main__":
    main()
