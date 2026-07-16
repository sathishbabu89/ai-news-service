from app.adapters.rss.arxiv_adapter import ArxivAdapter

adapter = ArxivAdapter(
    "https://rss.arxiv.org/rss/cs.AI"
)

articles = adapter.fetch_articles()

print(f"Total Articles: {len(articles)}")

print()

print(articles[0])