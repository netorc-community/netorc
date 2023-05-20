"""
manage.py
"""
import getpass
import sys

from passlib.hash import pbkdf2_sha256
from sqlmodel import SQLModel

from core import db
from core.db import tables
from core.metrics.logging import logger


def main(session=next(db.get_session())):
    if "migrate" in sys.argv[1]:
        SQLModel.metadata.create_all(db.engine)

    if "createsuperuser" in sys.argv[1]:
        try:
            superuser = tables.User()
            superuser.username = input("username: ")

            password = getpass.getpass(prompt="password: ")
            superuser.password = pbkdf2_sha256.hash(password)

            api_key = getpass.getpass(prompt="api key: ")
            superuser.api_key = pbkdf2_sha256.hash(api_key)

            session.add(superuser)
            session.commit()

            print(f"Superuser: {superuser.username}, created")
            logger.info("Superuser: %s, created", superuser.username)

        except Exception as exc:
            raise exc


if __name__ == "__main__":
    main()
