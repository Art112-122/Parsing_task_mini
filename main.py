from pydantic import HttpUrl
from fastapi import FastAPI, HTTPException, Query
import httpx
from bs4 import BeautifulSoup
from typing import Dict, Any
from bs4 import BeautifulSoup
import asyncio
import uvicorn

app = FastAPI(title="Parse anime")

@app.get("/parse/")
async def parse_url(url: HttpUrl = Query(..., description="URL to parse")) -> Dict[str, Any]:
    async with httpx.AsyncClient(timeout=10.0) as client:
        try:

            response = await client.get(str(url))
            response.raise_for_status()
        except httpx.RequestError as exc:
            raise HTTPException(status_code=400, detail=f"Request error for {url}: {str(exc)}")
        except httpx.HTTPStatusError as exc:
            raise HTTPException(status_code=exc.response.status_code,
                                detail=f"Error response {exc.response.status_code} while requesting {url}")

    soup = BeautifulSoup(response.text, "html.parser")

if __name__ == "__main__":
    uvicorn.run("main:app", port=8006, reload=True)
