"""
tmf653.py
"""
from fastapi import APIRouter

router = APIRouter(
    prefix="/tmf-api/servicetestmanagement/v1", tags=["TMF653 Service Test Management"]
)


@router.get("/servicetest")
async def get_service_test(id: int, description: str, mode: str, state: str) -> list:
    # Database to store service tests, retirve the test from the database
    pass


@router.post("/servicetest")
async def post_service_test():
    # Execute func, store the data in a database, or redis
    pass
