"""
manage.py
"""
from datetime import datetime
import sys
from sqlmodel import SQLModel, Session
from miscellaneous.database.db import engine
from miscellaneous.database.models import User, Service, ServiceType

TestService = Service(id="GN001", name="test", description="test", service_type="test", category="test", state="up",
                      start_date=datetime.now(), end_date=datetime.now())


def main():
    if "migrate" in sys.argv:
        SQLModel.metadata.create_all(engine)

    # with Session(engine) as SessionLocal:
    #     SessionLocal.add(TestService)
    #     SessionLocal.commit()
    #     SessionLocal.close()


if __name__ == "__main__":
    main()
