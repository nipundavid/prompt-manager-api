# app/main.py
from fastapi import FastAPI, status
from app.routes.v1.router import router
from app.constants import project
from contextlib import asynccontextmanager
from app.services.prompt_manager import PromptManager

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan_event(app: FastAPI):
    logger.info("Application startup")
    app.state.prompt_manager = PromptManager()
    yield
    app.state.prompt_manager = None
    logger.info("Application shutdown")

def create_application() -> FastAPI:
    logger.info("Start Application")
    application = FastAPI(
        title=project.TITLE,
        version="1.0.0",
        docs_url=f"{project.API_PREFIX}/docs",
        lifespan=lifespan_event
    )
    
    # Include the consolidated API router
    application.include_router(router, prefix=project.API_PREFIX)

    return application

app = create_application()

@app.get("/", status_code=status.HTTP_200_OK)
def health_check():
    return {"status": "server is up and running..."}