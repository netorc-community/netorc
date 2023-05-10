"""
manage.py
"""
import sys
from sqlmodel import SQLModel, Session
from miscellaneous.database.db import engine
from miscellaneous.database import tables


Default = tables.User(email="test", username="test", password="test", api_key="$pbkdf2-sha256$29000$CUEIAQAAwBjD.F/LWSsF4A$.zq9lWzf3/2BKZM6u.tIxU2wXOZzL5ERDOMtprpMpl8")

def main():
    if "migrate" in sys.argv:
        SQLModel.metadata.create_all(engine)  # Creates all the tables in the database

    with Session(engine) as session:
        session.add(Default)
        session.commit()
        session.close()

if __name__ == "__main__":
    main()


# with Session(engine) as SessionLocal:
#     SessionLocal.add(TestService)
#     SessionLocal.commit()
#     SessionLocal.close()

#
# TestService = Service(id="GN001", name="test", description="test", service_type="test", category="test", state="up",
#                       start_date=datetime.now(), end_date=datetime.now())
