from fastapi import FastAPI, HTTPException, Query
import uvicorn
from typing import Literal
from parsing import get_url, get_anime, get_anime_info

app = FastAPI(title="Parse anime")
BASIC_URL = "https://jut.su/anime/"


@app.get("/parse/")
async def parse_url(url: str = Query(..., description="URL to parse"),
                    _class: str = Query("", description="Find for class"),
                    tag: str = Query("", description="Find for tag")):
    answer = await get_url(url, _class, tag)
    return answer


@app.get("/anime/{category}")
async def anime(
        category: Literal[
            "adventure", "action", "comedy", "everyday", "romance", "drama", "fantastic", "fantasy", "mystic", "detective", "psychology"]):
    url = f"{BASIC_URL}{category}/"
    answer = await get_anime(url=url)
    return answer


@app.get("/anime/info/")
async def anime_info(title: str = Query(..., description="Название аниме")):
    answer = await get_anime_info(title)
    return answer


if __name__ == "__main__":
    uvicorn.run("main:app", port=8009, reload=True)
