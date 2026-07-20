import aiohttp


NEWS_API = "https://hn.algolia.com/api/v1/search_by_date?tags=story&query=AI"


async def fetch_ai_news():

    async with aiohttp.ClientSession() as session:

        async with session.get(NEWS_API) as response:

            if response.status != 200:
                return []

            data = await response.json()

    news = []

    for item in data["hits"][:10]:

        news.append(
            {
                "title": item.get("title", ""),
                "author": item.get("author", ""),
                "url": item.get("url", ""),
                "created_at": item.get("created_at", "")
            }
        )

    return news