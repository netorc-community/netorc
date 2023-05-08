from typing import Any
from fastapi import Response, Depends


async def general_http_headers(response: Response) -> Any:
    response.headers["cache-control"] = "no-cache, no-store"


require_general_http_headers = Depends(general_http_headers)
