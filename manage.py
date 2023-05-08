"""
manage.py
"""
import sys
from sqlmodel import SQLModel, Session
from miscellaneous.database.db import engine
from miscellaneous.database.models import UserModel

TestUser = UserModel(firstname="antonio", lastname="faria", email="antonio@something.com", username="antonio",
                     password="password123", password_salt="salt", api_key="api-key-1", api_key_salt="salt")


def main():
    if "migrate" in sys.argv:
        SQLModel.metadata.create_all(engine)

    with Session(engine) as SessionLocal:
        SessionLocal.add(TestUser)
        SessionLocal.commit()
        SessionLocal.close()


if __name__ == "__main__":
    main()
