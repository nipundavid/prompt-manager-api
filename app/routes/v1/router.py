from fastapi import APIRouter
from . import prompt

router = APIRouter()

router.include_router(prompt.router, prefix="/prompts", tags=["Prompts"])
