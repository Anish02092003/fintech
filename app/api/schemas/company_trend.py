from pydantic import BaseModel
from typing import List, Dict


class CompanyTrendRequest(BaseModel):
    company: str
    financials: List[Dict]


class CompanyTrendResponse(BaseModel):
    company: str
    overall_trend: str
    trends: Dict[str, str]
    confidence: str