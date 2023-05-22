"""
service.py
"""
from typing import List

from fastapi import APIRouter, Depends
from sqlmodel import Session, select

from core.addons.exceptions import APIError
from core.db import get_session
from core.db.tables import Service

router = APIRouter(
    prefix="/api/services/v1",
    tags=["Services"],
)


@router.get("/service", response_model=List[Service])
def get_service(id: str = None, session: Session = Depends(get_session)) -> list:
    """
    Returns a list of service/'s from the db.
    Arguments can be included in the uri to be added to the db query.

    Args:
        id: an optional service id filter.
        session: db session dependency.

    Returns:
        A list of dictionary/s containing attributes for a service.

    Raises:
        APIException: 500 status code.
    """
    try:
        if id is not None:
            service = session.get(Service, id)
            if not service:
                raise APIError(status_code=404, code="tbd", reason="tbd")
            return [service]

        query = select(Service)
        result = session.exec(query)
        return [x for x in result]

    except APIError:
        raise

    except Exception as exc:
        raise APIError(status_code=500, code="tbd", reason="tbd") from exc


@router.post("/service", response_model=List[Service])
async def post_service(service: Service) -> list:
    """
    Creates new service/s. The service/s is added to the db once the task completes.

    Args:

    Returns:

    Raises:
    """
    return []


@router.patch("/service/{id}", response_model=Service)
async def patch_service(id: int) -> list:
    """
    Amend a service. The service is updated in the db once the task completes.

    Args:

    Returns:

    Raises:
    """
    return []


@router.delete("/service/{id}", response_model=Service)
async def delete_service(id: int) -> list:
    """
    Remove a service. The service is deleted in the db once the task completes.

    Args:

    Returns:

    Raises:
    """
    return []
