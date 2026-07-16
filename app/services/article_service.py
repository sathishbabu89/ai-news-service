from app.adapters.rss.arxiv_adapter import ArxivAdapter


class ArticleService:

    def get_articles(self, limit: int = 10):

        adapter = ArxivAdapter(
            "https://rss.arxiv.org/rss/cs.AI"
        )

        return adapter.fetch_articles(limit)