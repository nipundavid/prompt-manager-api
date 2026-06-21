from fastapi import APIRouter
from app.routes.v1 import prompt

router = APIRouter()

router.include_router(prompt.router, prefix="/prompts", tags=["Prompts"])
