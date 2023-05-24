"""
manage.py
"""
import argparse
import getpass

from core.db import tables, migrate
from core.security import secret
from core.security.user import create_user


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["migrate", "createsuperuser"])
    args = parser.parse_args()

    if args.action == "migrate":
        migrate.migrate()

    if args.action == "createsuperuser":
        superuser = tables.User()
        superuser.username = input("Username: ")

        while True:
            password = getpass.getpass(prompt="Password: ")
            if not secret.validator(password):
                print("Password does not meet security requirements, please try again.")
            else:
                superuser.password = password
                break

        while True:
            api_key = getpass.getpass(prompt="API key: ")
            if not secret.validator(api_key):
                print("API key does not meet security requirements, please try again.")
            else:
                superuser.api_key = api_key
                break

        try:
            db_superuser = create_user(superuser)
            print(f"User: {db_superuser.username}, created.")

        except Exception:
            raise


if __name__ == "__main__":
    main()
