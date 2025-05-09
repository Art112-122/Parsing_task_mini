import httpx
from bs4 import BeautifulSoup
import asyncio

async def get_url(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            titles = soup.find_all("a", class_="storylink")
            return titles
        return []

if __name__ == "__main__":
    url = "https://news.ycombinator.com/"
    titles = asyncio.run(get_url(url))
    for i, title in enumerate(titles, 1):
        print(f"{i}. {title.text}")
