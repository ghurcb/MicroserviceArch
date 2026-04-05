from __future__ import annotations

from fastapi import FastAPI

from src.api.v1.articles.router import router as articles_router
from src.api.v1.comments.router import router as comments_router
from src.api.v1.users.router import router as users_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="Microservice FastAPI",
        version="1.0.0",
        description="Микросервисное приложение: пользователи, статьи, комментарии",
        docs_url="/docs",
        openapi_url="/openapi.json",
    )

    @app.api_route("/", methods=["GET", "HEAD"])
    async def root():
        return {"status": "ok", "service": "backend-api"}

    @app.get("/health", tags=["Health"])
    async def root():
        return {"status": "ok", "service": "backend-api"}

    app.include_router(articles_router, prefix="/api")
    app.include_router(comments_router, prefix="/api")
    app.include_router(users_router, prefix="/api")

    return app


app = create_app()
