from fastapi import APIRouter, Query

from app.services.research_service import ResearchService


router = APIRouter()


service = ResearchService()



@router.get("/research")
def get_research_digest(
    limit: int = Query(default=5, le=20)
):

    return {

        "latest": service.get_latest_research(
            limit
        ),

        "trending": service.get_trending_research(
            limit
        )

    }