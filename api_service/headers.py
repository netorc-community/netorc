from typing import Any

from fastapi import Response, Depends, Security
from fastapi.security.api_key import APIKeyHeader
from passlib.hash import pbkdf2_sha256
from sqlmodel import Session, select

from miscellaneous.addons.exceptions import APIException
from miscellaneous.database.db import get_session
from miscellaneous.database.tables import User
from settings import settings


async def general_http_headers(response: Response) -> Any:
    response.headers["cache-control"] = "no-cache, no-store"


require_general_http_headers = Depends(general_http_headers)

api_key_header = APIKeyHeader(name=settings.api_key_header, auto_error=False)


def general_authentication_header(api_key: str = Security(api_key_header),
                                  session: Session = Depends(get_session)) -> Any:
    """
    Retrieves api key in request header and checks api key exists in user database.

    Args:
        api_key: request api key
        session: database session dependency.

    Raises:
        APIException: 401 and 500 status codes.
    """
    try:
        query = select(User)
        result = session.exec(query).all()
        check = [x.api_key for x in result if
                 x.api_key.startswith("$pbkdf2-sha256") and pbkdf2_sha256.verify(api_key, x.api_key)]
        # Delay is caused if key is not in the pbkdf2 format passlib expects.
        if not check:
            raise APIException(status_code=401, code="tbd", reason="tbd")
    except Exception as exc:
        raise APIException(status_code=500, code="tbd", reason="tbd") from exc


require_general_authentication_header = Depends(general_authentication_header)
