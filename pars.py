import httpx
from bs4 import BeautifulSoup
import asyncio

async def get_url(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            answer = soup.find_all("span", class_="the_invis")
            return answer
        return []

url = "https://jut.su/anime/"
headings = asyncio.run(get_url(url))

for i, h in enumerate(headings, 1):
    print(f"{i}. {h.text.strip()}")

