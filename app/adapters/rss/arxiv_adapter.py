from typing import List

import feedparser

from app.adapters.base_adapter import BaseAdapter
from app.models.article import Article


class ArxivAdapter(BaseAdapter):

    def __init__(self, feed_url: str):
        self.feed_url = feed_url

    def fetch_articles(self, limit: int = 10) -> List[Article]:

        feed = feedparser.parse(self.feed_url)

        articles = []

        for entry in feed.entries[:limit]:

            # Clean the summary by removing arXiv-specific prefix
            summary = entry.summary

            if "Abstract:" in summary:
                summary = summary.split("Abstract:", 1)[1].strip()

            article = Article(
                id=entry.id.split(":")[-1],
                title=entry.title,
                summary=summary,
                authors=[
                    author.name for author in entry.authors
                ] if hasattr(entry, "authors") else [],
                published=entry.published,
                categories=[
                    tag.term for tag in entry.tags
                ] if hasattr(entry, "tags") else [],
                url=entry.link,
                source="arXiv"
            )

            articles.append(article)

        return articles