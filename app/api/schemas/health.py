from pydantic import BaseModel
from typing import Dict, List, Optional


class HealthScoreResponse(BaseModel):
    score: int
    risk_level: str
    accuracy: str
    components: Dict[str, int]
    signals: List[str]
    missing_components: Optional[List[str]] = None