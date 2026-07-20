import aiohttp

JOBS_API = "https://remoteok.com/api"


async def fetch_ai_jobs():
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(JOBS_API) as response:

            if response.status != 200:
                return []

            data = await response.json()

    jobs = []

    for item in data[1:]:
        position = str(item.get("position", "")).lower()

        if any(keyword in position for keyword in [
            "ai",
            "machine learning",
            "llm",
            "python",
            "data"
        ]):

            jobs.append({
                "company": item.get("company", ""),
                "position": item.get("position", ""),
                "location": item.get("location", ""),
                "url": item.get("url", "")
            })

        if len(jobs) >= 10:
            break

    return jobs