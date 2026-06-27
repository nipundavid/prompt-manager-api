from pathlib import Path
from typing import Any, Dict, List
import json
import logging
logger = logging.getLogger(__name__)

FILE_PATH = Path(__file__).parent.parent.parent / "prompts" / "prompts.json"

def load_prompts() -> List[Dict[str, Any]]:
    try:
        with open(FILE_PATH, "r") as f:
            return json.load(f)
    except FileNotFoundError as e:
        logger.error(f"Prompts file not found: {e}")
        return []