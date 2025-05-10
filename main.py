from fastapi import FastAPI, HTTPException, Query
import httpx
from typing import Dict, Any, Literal
from bs4 import BeautifulSoup
import uvicorn
from parsing import get_url, get_anime

app = FastAPI(title="Parse anime")

BASIC_URL = "https://jut.su/anime/"


@app.get("/parse/")
async def parse_url(url: str = Query(..., description="URL to parse"),
                    _class: str = Query("", description="Find for class"),
                    tag: str = Query("", description="Find for tag")):
    answer = await get_url(url, _class, tag)
    return answer


if __name__ == "__main__":
    uvicorn.run("main:app", port=8006, reload=True)


@app.get("/anime/{category}")
async def anime(
        category: Literal[
            "adventure", "action", "comedy", "everyday", "romance", "drama", "fantastic", "fantasy", "mystic", "detective", "psychology"]):
    url = f"{BASIC_URL}{category}/"
    answer = await get_anime(url=url)
    return answer
