from typing import Any

from fastapi import Response, Depends, Security
from fastapi.security.api_key import APIKeyHeader
from passlib.hash import pbkdf2_sha256
from sqlmodel import Session, select

from core.addons.exceptions import APIError
from core.db import require_db_session
from core.db.tables import User
from settings import settings


async def general_http_headers(response: Response) -> Any:
    """
    Adds keys,values to response headers. E.g, Cache-Control

    Args:
        response: starlette response object

    Returns:
        None

    """
    response.headers["cache-control"] = "no-cache, no-store"


require_general_http_headers = Depends(general_http_headers)

api_key_header = APIKeyHeader(name=settings.api_key_header, auto_error=False)


def general_authentication_header(api_key: str = Security(api_key_header),
                                  session: Session = Depends(require_db_session)) -> Any:
    """
    Retrieves api key in request header and checks api key exists in user db.

    Args:
        api_key: request api key
        session: db session dependency.

    Raises:
        APIException: 401 and 500 status codes.
    """
    try:
        if not api_key:
            raise APIError(status_code=401, code="General Authentication Header", reason="Unauthorised request")

        query = select(User)
        result = session.exec(query).all()
        check = [x.api_key for x in result if
                 x.api_key.startswith("$pbkdf2-sha256") and pbkdf2_sha256.verify(api_key, x.api_key)]

        if not check:
            raise APIError(status_code=401, code="General Authentication Header", reason="Unauthorised request")

    except APIError:
        raise

    except Exception as exc:
        raise APIError(status_code=500, code="General Authentication Header", reason="Runtime error occurred") from exc


require_general_authentication_header = Depends(general_authentication_header)
