from fastapi import APIRouter, Query

from app.adapters.api.huggingface_adapter import HuggingFaceAdapter


router = APIRouter()


@router.get("/huggingface/articles")
def get_huggingface_articles(
    limit: int = Query(default=5, le=20)
):

    adapter = HuggingFaceAdapter()

    articles = adapter.fetch_articles(
        limit=limit
    )

    return articles