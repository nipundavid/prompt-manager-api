# app/api/v1/endpoints/users.py
from fastapi import APIRouter, Depends, HTTPException, status, Request
router = APIRouter()

def get_prompts_from_state(request: Request) -> list:
    return request.app.state.prompts

def get_prompt_by_prompt_id(prompt_id: str, request: Request):
    prompts = get_prompts_from_state(request)
    for prompt in prompts:
        if prompt.get("prompt_id") == prompt_id:
            return prompt
    return None

@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_prompts(prompts:list = Depends(get_prompts_from_state)):
    return prompts

@router.get("/{prompt_id}")
async def get_prompt(prompt_id: str, request: Request):
    prompt = get_prompt_by_prompt_id(prompt_id, request)
    if not prompt:
        raise HTTPException(status_code=404, detail="Prompt not found")
    return {**prompt}

@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_prompt(prompt: dict):
    return {"prompt_id": 2, **prompt}  

@router.put("/{prompt_id}", status_code=status.HTTP_200_OK)
async def update_prompt(prompt_id: int, prompt: dict):
    if prompt_id != 1:
        raise HTTPException(status_code=404, detail="Prompt not found")
    return {"prompt_id": prompt_id, **prompt} 

@router.delete("/{prompt_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_prompt(prompt_id: int): 
    if prompt_id != 1:
        raise HTTPException(status_code=404, detail="Prompt not found")
    return {"message": "Prompt deleted successfully"}