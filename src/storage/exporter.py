import os
import pandas as pd

EXPORT_FOLDER = "exports"

os.makedirs(EXPORT_FOLDER, exist_ok=True)


def export_startups(startups):
    df = pd.DataFrame(startups)
    filename = os.path.join(EXPORT_FOLDER, "startups.csv")
    df.to_csv(filename, index=False)
    print(f"Startups exported -> {filename}")


def export_products(products):
    df = pd.DataFrame(products)
    filename = os.path.join(EXPORT_FOLDER, "products.csv")
    df.to_csv(filename, index=False)
    print(f"Products exported -> {filename}")


def export_papers(papers):
    df = pd.DataFrame(papers)
    filename = os.path.join(EXPORT_FOLDER, "papers.csv")
    df.to_csv(filename, index=False)
    print(f"Papers exported -> {filename}")


def export_news(news):
    df = pd.DataFrame(news)
    filename = os.path.join(EXPORT_FOLDER, "news.csv")
    df.to_csv(filename, index=False)
    print(f"News exported -> {filename}")


def export_jobs(jobs):
    df = pd.DataFrame(jobs)
    filename = os.path.join(EXPORT_FOLDER, "jobs.csv")
    df.to_csv(filename, index=False)
    print(f"Jobs exported -> {filename}")