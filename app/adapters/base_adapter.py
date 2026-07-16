from abc import ABC, abstractmethod
from typing import List

from app.models.article import Article


class BaseAdapter(ABC):

    @abstractmethod
    def fetch_articles(self) -> List[Article]:
        """
        Fetch articles from a source.
        """
        pass