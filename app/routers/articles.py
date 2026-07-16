from fastapi import APIRouter, Query

from app.services.article_service import ArticleService

router = APIRouter()


@router.get("/articles")
def get_articles(limit: int = Query(default=10, ge=1, le=100)):

    service = ArticleService()

    return service.get_articles(limit)