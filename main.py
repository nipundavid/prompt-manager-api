# app/main.py
from fastapi import FastAPI
from app.routes.v1.router import router
from app.constants import project
from app.services.prompt_loader import load_prompts

import logging
logger = logging.getLogger(__name__)

def create_application() -> FastAPI:
    application = FastAPI(
        title=project.TITLE,
        version="1.0.0",
        docs_url=f"{project.API_PREFIX}/docs"
    )
    
    # Include the consolidated API router
    application.include_router(router, prefix=project.API_PREFIX)

    logger.info(load_prompts())
    
    return application

app = create_application()