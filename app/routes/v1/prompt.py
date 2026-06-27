# app/api/v1/endpoints/users.py
from fastapi import APIRouter, HTTPException, status
router = APIRouter()



@router.get("/", status_code=status.HTTP_200_OK)
async def get_all_prompts():
    return [{"prompt_id": 1, "title": "Hello, World!"," content": "This is a sample prompt.", "category": "Sample"}]

@router.get("/{prompt_id}")
async def get_prompt(prompt_id: int):
    if prompt_id != 1:
        raise HTTPException(status_code=404, detail="Prompt not found")
    return {"prompt_id": prompt_id, "title": "Hello, World!", "content": "This is a sample prompt.", "category": "Sample"}

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