"""
manage.py
"""
import sys
import getpass

from sqlmodel import SQLModel
from passlib.hash import pbkdf2_sha256

from core import db
from core.db import tables


def main(session=next(db.get_session())):
    if "migrate" in sys.argv[1]:
        SQLModel.metadata.create_all(db.engine)

    if "createsuperuser" in sys.argv[1]:
        superuser = tables.User()
        superuser.username = input("username: ")
        password = getpass.getpass(prompt="password: ")
        superuser.password = pbkdf2_sha256.hash(password)
        api_key = getpass.getpass(prompt="api key: ")
        superuser.api_key = pbkdf2_sha256.hash(api_key)
        session.add(superuser)
        session.commit()


if __name__ == "__main__":
    main()
