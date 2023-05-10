"""
manage.py
"""
import sys

from sqlmodel import SQLModel

from miscellaneous.database.db import engine


def main():
    if "migrate" in sys.argv:
        SQLModel.metadata.create_all(engine)  # Creates all the tables in the database


if __name__ == "__main__":
    main()
