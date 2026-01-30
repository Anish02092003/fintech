from pydantic import BaseModel
from typing import Dict, Any


class ExplainRequest(BaseModel):
    context: Dict[str, Any]   # health score or simulation output
    question: str             # "Why did my score drop?"


class ExplainResponse(BaseModel):
    explanation: str
    confidence: str
    assumptions: list[str]