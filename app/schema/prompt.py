from pydantic import BaseModel

class Prompt(BaseModel):
    title: str
    content: str
    category: str