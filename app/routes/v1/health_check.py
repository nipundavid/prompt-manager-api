from fastapi import APIRouter, status, HTTPException
router = APIRouter()

@router.get("/health", status_code=status.HTTP_200_OK)
def health_check():
    return {"status": "healthy"}
