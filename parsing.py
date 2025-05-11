import httpx
from bs4 import BeautifulSoup
from fastapi import HTTPException

BASIC_URL = "https://jut.su/name/"

async def get_url(url, _class: str | None = None, tag: str | None = None):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            if _class:
                if tag:
                    answer = soup.find_all(tag, class_=_class)
                    return {"answer": [str(tag) for tag in answer]}
                answer = soup.find_all(class_=_class)
                return {"answer": [str(tag) for tag in answer]}
            elif tag:
                answer = soup.find_all(tag)
                return {"answer": [str(tag) for tag in answer]}
            answer = soup.find_all()
            return {"answer": [str(tag) for tag in answer]}
        raise HTTPException(status_code=response.status_code, detail=response.text)

async def get_anime(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            answer = soup.find_all("span", class_="the_invis")
            return {
                "answer": [
                    f"{i} {a.text}: {BASIC_URL}{a.find('a').get('href')}"
                    for i, a in enumerate(answer, 1)
                ]
            }
        raise HTTPException(status_code=response.status_code, detail=response.text)


async def get_anime_info(title: str):
    url = f"https://jut.su/{title}/"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Находим все эпизоды
            episodes = soup.find_all("a", class_="one_manga_page_link")
            total = len(episodes)

            return {
                "title": title,
                "total_episodes": total
            }

    raise HTTPException(status_code=response.status_code, detail=response.text)

