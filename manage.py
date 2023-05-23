"""
manage.py
"""
import argparse
import getpass

from core.db import tables, migrate
from core.security import secret, user


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("action", choices=["migrate", "createsuperuser"])
    args = parser.parse_args()

    if args.action == "migrate":
        migrate.migrate()

    if args.action == "createsuperuser":
        superuser = tables.User()
        superuser.username = input("username: ")

        while True:
            password = getpass.getpass(prompt="password: ")
            if not secret.validator(password):
                print("Password does not meet security requirements, please try again.")
            else:
                superuser.password = password
                break

        while True:
            api_key = getpass.getpass(prompt="api key: ")
            if not secret.validator(api_key):
                print("API key does not meet security requirements, please try again.")
            else:
                superuser.api_key = api_key
                break

        if user.create_user(superuser) is True:
            print(f"User: {superuser.username}, created.")


if __name__ == "__main__":
    main()
