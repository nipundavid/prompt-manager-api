from fastapi import APIRouter, Depends, HTTPException, status, Request
from app.schema.prompt import Prompt
from app.services.prompt_manager import PromptManager
router = APIRouter()

def get_prompt_manager(request: Request) -> PromptManager:
    return request.app.state.prompt_manager

@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_prompts(prompt_manager:PromptManager = Depends(get_prompt_manager)):
    return prompt_manager.prompts

@router.get("/{prompt_id}")
async def get_prompt(prompt_manager: PromptManager = Depends(get_prompt_manager), prompt_id: str = None):
    prompt = prompt_manager.get_prompt_by_prompt_id(prompt_id)
    if not prompt:
        raise HTTPException(status_code=404, detail="Prompt not found")
    return {**prompt}

@router.post("/", status_code=status.HTTP_201_CREATED)
async def save_new_prompt(prompt_manager:PromptManager = Depends(get_prompt_manager), prompt: Prompt = None):
    prompt_dict = prompt.model_dump()  # Convert Pydantic model to dictionary
    prompt_id = prompt_manager.save_new_prompt(prompt_dict)
    if not prompt_id:
        raise HTTPException(status_code=500, detail="Failed to save the prompt")
    return {"prompt_id": prompt_id}
   