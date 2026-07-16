from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware

from app.routers.articles import router as article_router


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


app.include_router(
    article_router,
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