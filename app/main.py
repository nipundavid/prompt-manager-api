# app/main.py
from fastapi import FastAPI
from app.routes.v1.router import router
from app.constants import project
from app.services.prompt_loader import load_prompts
from contextlib import asynccontextmanager

import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def _load_prompts():
    prompts = load_prompts()
    logger.info(f"Loaded {len(prompts)} prompts.")

@asynccontextmanager
async def lifespan_event(app: FastAPI):
    logger.info("Application startup")
    _load_prompts()
    yield
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