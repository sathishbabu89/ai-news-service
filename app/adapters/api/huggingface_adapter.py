import os
from typing import List

import requests
from dotenv import load_dotenv

from app.adapters.base_adapter import BaseAdapter
from app.models.article import Article


load_dotenv()


class HuggingFaceAdapter(BaseAdapter):

    def __init__(self):

        self.url = "https://huggingface.co/api/daily_papers"

        self.headers = {
            "Authorization": f"Bearer {os.getenv('HF_TOKEN')}"
        }


    def fetch_articles(
        self,
        limit: int = 10,
        sort: str = "trending"
    ) -> List[Article]:


        response = requests.get(
            self.url,
            headers=self.headers,
            params={
                "limit": limit,
                "sort": sort
            }
        )

        response.raise_for_status()


        papers = response.json()


        articles = []


        for item in papers:


            paper = item["paper"]


            article = Article(

                id=paper["id"],

                title=paper["title"],

                summary=paper["summary"],

                authors=[
                    author["name"]
                    for author in paper.get("authors", [])
                ],

                published=paper["publishedAt"],

                categories=[
                    "AI Research",
                    "Hugging Face"
                ],

                url=(
                    paper.get("projectPage")
                    or
                    f"https://huggingface.co/papers/{paper['id']}"
                ),

                source="Hugging Face"

            )


            articles.append(article)


        return articles