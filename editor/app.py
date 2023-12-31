from fastapi import APIRouter, FastAPI

from editor.apps.analyzer.router import router as analyzer_router


def get_router() -> APIRouter:
    """Get main router with app routers included inside."""

    router = APIRouter()
    router.include_router(router=analyzer_router, prefix="/analyzer")
    return router


def get_app() -> FastAPI:
    """Get FastAPI application."""

    router = get_router()

    app = FastAPI()
    app.include_router(router=router, prefix="/api/v1.0.0")

    return app
