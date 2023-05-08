from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from miscellaneous.addons.exceptions import APIException
from api_service.service import activation

fastapi = FastAPI()
fastapi.include_router(activation.router)


@fastapi.exception_handler(APIException)
async def exception_handler(request: Request, exc: APIException):
    # Optional
    if None not in (
        exc.message,
        exc.reference_error,
        exc.class_type,
        exc.schema_location,
    ):
        return JSONResponse(
            status_code=exc.status_code,
            content={
                "code": exc.code,
                "reason": exc.reason,
                "message": exc.message,
                "status": exc.status_code,
                "referenceError": exc.reference_error,
                "@type": exc.class_type,
                "@schemaLocation": exc.schema_location,
            },
        )
    # Mandatory
    return JSONResponse(
        status_code=exc.status_code,
        content={"code": exc.code, "reason": exc.reason},
    )
