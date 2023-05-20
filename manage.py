"""
manage.py
"""
import argparse
import getpass

from passlib.hash import pbkdf2_sha256
from sqlmodel import SQLModel

from core import db
from core.db import tables
from core.metrics.logging import logger
from core.security import secret


def main(session=next(db.get_session())):
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["migrate", "createsuperuser"])
    args = parser.parse_args()

    if args.action == "migrate":
        SQLModel.metadata.create_all(db.engine)
        logger.info("Successfully migrated tables to database")

    if args.action == "createsuperuser":
        superuser = tables.User()
        superuser.username = input("username: ")

        while True:
            password = getpass.getpass(prompt="password: ")
            if not secret.validator(password):
                print("Password does not meet security requirements, please try again.")
            else:
                break

        while True:
            api_key = getpass.getpass(prompt="api key: ")
            if not secret.validator(api_key):
                print("API key does not meet security requirements, please try again.")
            else:
                break

        superuser.password = pbkdf2_sha256.hash(password)
        superuser.api_key = pbkdf2_sha256.hash(api_key)

        try:
            session.add(superuser)
            session.commit()

        except Exception as exc:
            logger.error("Error creating superuser: %s", exc)
            raise

        logger.info("Superuser: %s, created", superuser.username)


if __name__ == "__main__":
    main()
