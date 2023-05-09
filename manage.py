"""
manage.py
"""
import sys
from sqlmodel import SQLModel
from miscellaneous.database.db import engine
from miscellaneous.database import tables


def main():
    if "migrate" in sys.argv:
        SQLModel.metadata.create_all(engine)  # Creates all the tables in the database


if __name__ == "__main__":
    main()


# with Session(engine) as SessionLocal:
#     SessionLocal.add(TestService)
#     SessionLocal.commit()
#     SessionLocal.close()

#
# TestService = Service(id="GN001", name="test", description="test", service_type="test", category="test", state="up",
#                       start_date=datetime.now(), end_date=datetime.now())
