from app.adapters.rss.arxiv_adapter import ArxivAdapter
from app.adapters.api.huggingface_adapter import HuggingFaceAdapter


class ResearchService:


    def __init__(self):

        self.arxiv_adapter = ArxivAdapter(
            "https://rss.arxiv.org/rss/cs.AI"
        )

        self.huggingface_adapter = HuggingFaceAdapter()



    def get_latest_research(self, limit: int = 5):

        return self.arxiv_adapter.fetch_articles(
            limit=limit
        )



    def get_trending_research(self, limit: int = 5):

        return self.huggingface_adapter.fetch_articles(
            limit=limit,
            sort="trending"
        )