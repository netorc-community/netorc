"""
activation.py
"""

from fastapi import APIRouter

router = APIRouter(
    prefix="/netorc-api/serviceactivation/v1",
    tags=["Service Activation"],
)


@router.get("/service")
async def get_service():
    pass


@router.post("/service")
async def post_service():
    pass


@router.patch("/service/{id}")
async def patch_service(id: int):
    pass


@router.delete("/service/{id}")
async def delete_service(id: int):
    pass
