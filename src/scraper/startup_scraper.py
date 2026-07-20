import aiohttp
from datetime import datetime

GITHUB_API = "https://api.github.com/search/repositories"

HEADERS = {
    "Accept": "application/vnd.github+json",
    "User-Agent": "GraphOne-Pipeline"
}


async def fetch_startups(page=1):
    startups = []

    params = {
        "q": "topic:artificial-intelligence",
        "sort": "stars",
        "order": "desc",
        "per_page": 100,
        "page": page
    }

    async with aiohttp.ClientSession(headers=HEADERS) as session:
        async with session.get(GITHUB_API, params=params) as response:

            if response.status != 200:
                print("GitHub API Error:", response.status)
                print(await response.text())
                return []

            data = await response.json()

    for repo in data.get("items", []):

        startups.append(
            {
                "schemaVersion": "1.0",
                "recordType": "STARTUP",
                "source": {
                    "name": "GitHub",
                    "url": repo["html_url"]
                },
                "content": {
                    "entityName": repo["owner"]["login"],
                    "data": {
                        "employeeCount": None
                    }
                },
                "collectedAt": datetime.utcnow().isoformat()
            }
        )

    print(f"Startups extracted : {len(startups)}")

    return startups