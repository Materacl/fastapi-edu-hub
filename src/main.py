import logging
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from api.v1 import router as api_v1_router
from config import settings

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def create_app() -> FastAPI:
    """
    Create and configure an instance of the FastAPI application.

    Returns:
        app (FastAPI): The configured FastAPI application.
    """

    app = FastAPI(
        title=settings.APP_TITLE,
        description=settings.APP_DESCRIPTION,
        version=settings.APP_VERSION,
        )

    # Include API v1 router
    app.include_router(api_v1_router, prefix="/api")

    @app.get("/")
    async def read_root():
        """
        Root endpoint that redirects to the API documentation.
        """
        return RedirectResponse(url="/docs")

    return app


# Create an instance of the FastAPI application
app = create_app()
