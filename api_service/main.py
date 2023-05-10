from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from api_service.headers import require_general_authentication_header
from api_service.services import service
from miscellaneous.addons.exceptions import APIException

fastapi = FastAPI(title="NetORC", version="0.0.1", dependencies=[require_general_authentication_header])
fastapi.include_router(service.router)


@fastapi.exception_handler(APIException)
async def exception_handler(request: Request, exc: APIException):
    """
    Exception handler for APIException. Ensures meaningful errors are sent to users/systems.

    Args:
        request: The request object.
        exc: APIException object.

    Returns:
        A json response body using attributes of the exc object.
    """

    # Optional attributes
    if None not in (
            exc.message,
            exc.reference_error,
    ):
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "code": exc.code,
                "reason": exc.reason,
                "message": exc.message,
                "status": exc.status_code,
                "referenceError": exc.reference_error,
            },
        )
    # Mandatory attributes
    return JSONResponse(
        status_code=exc.status_code,
        content={"code": exc.code, "reason": exc.reason},
    )
