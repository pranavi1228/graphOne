import aiohttp
import xml.etree.ElementTree as ET

BASE_URL = "http://export.arxiv.org/api/query"


async def fetch_latest_papers(total_results=1000):
    """
    Fetch AI research papers from arXiv using pagination.

    Args:
        total_results (int): Total number of papers to fetch.

    Returns:
        list[dict]: List of paper dictionaries.
    """

    papers = []

    namespace = {
        "atom": "http://www.w3.org/2005/Atom"
    }

    async with aiohttp.ClientSession() as session:

        # Fetch 100 papers at a time
        for start in range(0, total_results, 100):

            print(f"Fetching papers {start + 1} - {min(start + 100, total_results)}")

            params = {
                "search_query": "cat:cs.AI",
                "start": start,
                "max_results": 100,
                "sortBy": "submittedDate",
                "sortOrder": "descending",
            }

            async with session.get(BASE_URL, params=params) as response:

                if response.status != 200:
                    print(f"Failed to fetch batch starting at {start}. Status: {response.status}")
                    continue

                xml = await response.text()

            root = ET.fromstring(xml)

            for entry in root.findall("atom:entry", namespace):

                title = entry.find("atom:title", namespace)
                summary = entry.find("atom:summary", namespace)
                published = entry.find("atom:published", namespace)
                paper_url = entry.find("atom:id", namespace)

                authors = []

                for author in entry.findall("atom:author", namespace):
                    name = author.find("atom:name", namespace)
                    if name is not None:
                        authors.append(name.text)

                papers.append({
                    "title": title.text.strip() if title is not None else "",
                    "authors": authors,
                    "summary": summary.text.strip() if summary is not None else "",
                    "paper_url": paper_url.text if paper_url is not None else "",
                    "published": published.text if published is not None else "",
                })

    print(f"Total papers fetched: {len(papers)}")

    return papers