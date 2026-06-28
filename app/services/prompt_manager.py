from pathlib import Path
from typing import Any, Dict, List
import uuid
import json
import logging
logger = logging.getLogger(__name__)

FILE_PATH = Path(__file__).parent.parent.parent / "prompts" / "prompts.json"

class PromptManager:
    def __init__(self):
        self.prompts = self.load_prompts()

    def load_prompts(self) -> List[Dict[str, Any]]:
        try:
            with open(FILE_PATH, "r") as f:
                return json.load(f)
        except FileNotFoundError as e:
            logger.error(f"Prompts file not found: {e}")
            return []
        
    def get_prompt_by_prompt_id(self,prompt_id: str) -> Dict[str, Any]:
        for prompt in self.prompts:
            if prompt.get("prompt_id") == prompt_id:
                return prompt
        return None

    def save_new_prompt(self,prompt: List[Dict[str, Any]]) -> str:
        if not isinstance(prompt, dict):
            logger.error("Invalid prompt format. Expected a dictionary.")
            return None
        
        all_prompts = self.load_prompts()

        prompt_id = str(uuid.uuid4())
        prompt["prompt_id"] = prompt_id
        all_prompts.append(prompt)
        
        self.prompts = all_prompts  # Update the in-memory prompts list

        try:
            with open(FILE_PATH,"w") as f:
                json.dump(all_prompts, f, indent=2)
                return prompt_id
        except Exception as e:
            logger.error(f"Error saving prompt: {e}")
            return None