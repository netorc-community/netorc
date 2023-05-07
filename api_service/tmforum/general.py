"""
general.py
"""
from typing import Any
from fastapi import Response, Depends


async def tmf_general_http_headers(response: Response) -> Any:
    """TMF630 1.6"""
    response.headers["cache-control"] = "no-cache, no-store"


require_tmf_general_http_headers = Depends(tmf_general_http_headers)
