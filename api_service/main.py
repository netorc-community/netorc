"""
main.py
"""
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from miscellaneous.addons.exceptions import TMFException
from miscellaneous.addons.decorators import queue_task

from api_service.tmforum import tmf_653

from worker_service.tasks.example import example_task


fastapi = FastAPI()
fastapi.include_router(tmf_653.router)  # Service Test Management


@fastapi.exception_handler(TMFException)
async def tmf_exception_handler(request: Request, exc: TMFException):
    """TMF 630 3.4 global exception handler"""

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


@fastapi.get("/api")
async def example() -> list:
    task = queue_task(example_task)
    return [{"id": task.id}]
