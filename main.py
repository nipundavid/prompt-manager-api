# app/main.py
from fastapi import FastAPI
from app.routes.v1.router import router
from app.constants import project

def create_application() -> FastAPI:
    application = FastAPI(
        title=project.TITLE,
        version="1.0.0",
        docs_url="/docs"
    )
    
    # Include the consolidated API router
    application.include_router(router, prefix=project.API_PREFIX)
    
    return application

app = create_application()