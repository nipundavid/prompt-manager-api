from pathlib import Path
from typing import Any, Dict, List
import json

FILE_PATH = Path(__file__).parent.parent.parent / "prompts" / "prompts.json"

def load_prompts() -> List[Dict[str, Any]]:
    with open(FILE_PATH, "r") as f:
        return json.load(f)