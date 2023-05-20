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
from core.security.password import password_enforcer


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
            if not password_enforcer(password):
                print("Password does not meet security requirements, please try again.")
            else:
                break

        superuser.password = pbkdf2_sha256.hash(password)

        while True:
            api_key = getpass.getpass(prompt="api key: ")
            if not password_enforcer(api_key):
                print("API key does not meet security requirements, please try again.")
            else:
                break

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
