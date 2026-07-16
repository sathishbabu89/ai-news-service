from pydantic import BaseModel
from typing import List


class Article(BaseModel):
    id: str
    title: str
    summary: str
    authors: List[str]
    published: str
    categories: List[str]
    url: str
    source: str