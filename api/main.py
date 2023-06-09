from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles

from api.services import service, admin
from core.addons.exceptions import APIError

fastapi = FastAPI(title="NetORC", version="pre-release")
# from api.headers import require_general_authentication_header
# dependencies=[require_general_authentication_header]
fastapi.include_router(service.router)
fastapi.include_router(admin.router)
fastapi.mount("/static", StaticFiles(directory="api/landing/page"))


@fastapi.exception_handler(APIError)
async def exception_handler(request: Request, exc: APIError):
    """
    Exception handler for APIError. Ensures meaningful errors are sent to users/systems.

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


@fastapi.get("/", response_class=HTMLResponse)
async def landing_page():
    with open("api/landing/page/html/landing.html", "r") as html:
        return html.read()
