from pydantic import BaseModel
from typing import List, Dict


class CompanyExplainRequest(BaseModel):
    company: str
    overall_health: str
    scores: Dict[str, str]
    key_signals: List[str]


class CompanyExplainResponse(BaseModel):
    explanation: str
    confidence: str
    assumptions: List[str]