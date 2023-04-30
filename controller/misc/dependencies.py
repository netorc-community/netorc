from fastapi import Security, HTTPException, Depends, status
from fastapi.security.api_key import APIKeyHeader
from typing import Any, Annotated
from controller import settings

API_KEY_HEADER = APIKeyHeader(name=settings.API_KEY_HEADER, auto_error=False)

async def require_api_key(api_key: str = Security(API_KEY_HEADER)) -> Any:
    """Requires a specific API Key header and checks for
    the specific API Key configured in the settings"""
    if api_key not in settings.API_KEYS:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED)

# Shared Annotated Dependencies prevents the need to constantly use 'Depends' in every file
RequireAPIAuth = Annotated[APIKeyHeader, Depends(require_api_key)]