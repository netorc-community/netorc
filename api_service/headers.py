from passlib.hash import pbkdf2_sha256
from typing import Any
from fastapi import Response, Depends, Security
from fastapi.security.api_key import APIKeyHeader
from settings import settings
from sqlmodel import Session, select
from miscellaneous.database.db import engine
from miscellaneous.database.tables import User
from miscellaneous.addons.exceptions import APIException


async def general_http_headers(response: Response) -> Any:
    response.headers["cache-control"] = "no-cache, no-store"


require_general_http_headers = Depends(general_http_headers)

api_key_header = APIKeyHeader(name=settings.api_key_header, auto_error=False)


# TODO shared dependency for database session.

async def general_authentication_header(api_key: str = Security(api_key_header)) -> Any:
    try:
        with Session(engine) as session:
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
