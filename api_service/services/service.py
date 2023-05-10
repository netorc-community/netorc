"""
service.py
"""
from typing import List

from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from miscellaneous.addons.exceptions import APIException
from miscellaneous.database.db import get_session
from miscellaneous.database.tables import Service

router = APIRouter(
    prefix="/api/services/v1",
    tags=["Services"],
)


@router.get("/service", response_model=List[Service])
def get_service(id: str = None, session: Session = Depends(get_session)) -> list:
    """
    Returns a list of service/'s from the database.
    Arguments can be included in the uri to be added to the database query.

    Args:
        id: an optional service id filter.
        session: database session dependency.

    Returns:
        A list of dictionary/s containing attributes for a service.

    Raises:
        APIException: 500 status code.
    """
    try:
        if id is not None:
            service = session.get(Service, id)
            if not service:
                raise APIException(status_code=404, code="tbd", reason="tbd")
            return [service]

        query = select(Service)
        result = session.exec(query)
        return [x for x in result]

    except Exception as exc:
        raise APIException(status_code=500, code="tbd", reason="tbd") from exc


@router.post("/service", response_model=List[Service])
async def post_service(service: Service) -> list:
    """
    Creates new service/s. The service/s is added to the database once the task completes.

    Args:

    Returns:

    Raises:
    """
    return []


@router.patch("/service/{id}", response_model=Service)
async def patch_service(id: int) -> list:
    """
    Amend a service. The service is updated in the database once the task completes.

    Args:

    Returns:

    Raises:
    """
    return []


@router.delete("/service/{id}", response_model=Service)
async def delete_service(id: int) -> list:
    """
    Remove a service. The service is deleted in the database once the task completes.

    Args:

    Returns:

    Raises:
    """
    return []
