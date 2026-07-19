from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.articles import router as article_router
from app.routers.huggingface import router as huggingface_router
from app.routers.research import router as research_router

app = FastAPI(
    title="AI News Service",
    version="1.0.0"
)


# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():

    return {
        "message": "AI News Service is running."
    }


# Existing arXiv endpoint
app.include_router(
    article_router,
    prefix="/api/v1"
)


# New Hugging Face endpoint
app.include_router(
    huggingface_router,
    prefix="/api/v1"
)

app.include_router(
    research_router,
    prefix="/api/v1"
)

if __name__ == "__main__":

    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )