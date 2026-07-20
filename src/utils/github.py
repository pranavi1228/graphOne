import os
import aiohttp
from dotenv import load_dotenv

load_dotenv()

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")

GITHUB_API = "https://api.github.com/search/repositories"

print("GitHub Token Loaded:", bool(GITHUB_TOKEN))

# After a rate limit error, skip all remaining GitHub requests
github_available = True


async def search_github_repository(query: str):
    """
    Search GitHub for a repository related to a research paper.

    Returns:
    {
        "repo_name": "...",
        "repo_url": "...",
        "stars": 123
    }

    Returns None if nothing is found.
    """

    global github_available

    if not github_available:
        return None

    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "GraphOne-Pipeline"
    }

    if GITHUB_TOKEN:
        headers["Authorization"] = f"Bearer {GITHUB_TOKEN}"

    params = {
        "q": query,
        "per_page": 1
    }

    try:
        async with aiohttp.ClientSession(headers=headers) as session:

            print(f"Searching GitHub: {query}")

            async with session.get(GITHUB_API, params=params) as response:

                # Success
                if response.status == 200:

                    data = await response.json()

                    items = data.get("items", [])

                    if not items:
                        return None

                    repo = items[0]

                    return {
                        "repo_name": repo.get("full_name"),
                        "repo_url": repo.get("html_url"),
                        "stars": repo.get("stargazers_count", 0),
                    }

                # Rate limit
                elif response.status == 403:

                    print("\nGitHub Rate Limit Reached!")

                    error = await response.text()
                    print(error)

                    # Skip all remaining GitHub API calls
                    github_available = False

                    return None

                # Any other error
                else:

                    print(f"\nGitHub API Error: {response.status}")
                    print(await response.text())

                    return None

    except Exception as e:

        print(f"\nGitHub Search Exception: {e}")

        return None