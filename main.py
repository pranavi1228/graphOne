import asyncio

from src.scraper.startup_scraper import fetch_startups
from src.scraper.product_scraper import fetch_products
from src.scraper.paper_scraper import fetch_latest_papers
from src.scraper.news_scraper import fetch_ai_news
from src.scraper.jobs_scraper import fetch_ai_jobs

from src.storage.exporter import (
    export_startups,
    export_products,
    export_papers,
    export_news,
    export_jobs,
)

from src.utils.github import search_github_repository
from src.entity.resolver import canonicalize


async def main():

    print("=" * 80)
    print("GRAPHONE AI DATA PIPELINE")
    print("=" * 80)

    # ---------------- STARTUPS ----------------

    print("\nFetching Startups...\n")

    startups = []

    for page in range(1, 11):
        data = await fetch_startups(page)
        startups.extend(data)

    for startup in startups:
        startup["content"]["entityName"] = canonicalize(
            startup["content"]["entityName"]
        )

    export_startups(startups)

    print(f"Collected {len(startups)} startups.")

    # ---------------- PRODUCTS ----------------

    print("\nFetching Products...\n")

    products = await fetch_products(startups)

    export_products(products)

    print(f"Collected {len(products)} products.")

    # ---------------- PAPERS ----------------

    print("\nFetching AI Research Papers...\n")

    papers = await fetch_latest_papers(total_results=1000)

    print("\nSearching GitHub repositories...\n")

    github_limit = min(20, len(papers))

    for i in range(github_limit):

        github_repo = await search_github_repository(
            papers[i]["title"]
        )

        papers[i]["github"] = github_repo

        await asyncio.sleep(1)

    for i in range(github_limit, len(papers)):
        papers[i]["github"] = None

    export_papers(papers)

    print(f"Collected {len(papers)} papers.")

    # ---------------- NEWS ----------------

    print("\nFetching AI News...\n")

    news = await fetch_ai_news()

    export_news(news)

    print(f"Collected {len(news)} news articles.")

    # ---------------- JOBS ----------------

    print("\nFetching AI Jobs...\n")

    jobs = await fetch_ai_jobs()

    export_jobs(jobs)

    print(f"Collected {len(jobs)} jobs.")

    # ---------------- SUMMARY ----------------

    print("\n" + "=" * 80)
    print("PIPELINE SUMMARY")
    print("=" * 80)

    print(f"Startups : {len(startups)}")
    print(f"Products : {len(products)}")
    print(f"Papers   : {len(papers)}")
    print(f"News     : {len(news)}")
    print(f"Jobs     : {len(jobs)}")

    print("\nPipeline completed successfully!")


if __name__ == "__main__":
    asyncio.run(main())