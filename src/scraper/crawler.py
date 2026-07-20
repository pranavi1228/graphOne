import aiohttp
from src.utils.retry import async_retry

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/137.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en-US,en;q=0.9",
}


async def _fetch(session, url):
    async with session.get(url) as response:
        response.raise_for_status()
        return await response.text()


async def fetch_html(url: str):
    """
    Fetch HTML with retry support.
    """
    async with aiohttp.ClientSession(headers=HEADERS) as session:
        return await async_retry(_fetch, session, url)