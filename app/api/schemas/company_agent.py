from pydantic import BaseModel
from typing import Dict, List


class CompanyAgentResponse(BaseModel):
    company: str
    overall_health: str
    scores: Dict[str, str]
    key_signals: List[str]

    explanation: str
    confidence: str
    assumptions: List[str]