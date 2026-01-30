from pydantic import BaseModel
from typing import List, Dict


class CompanyTrendData(BaseModel):
    company: str
    financials: List[Dict]


class CompanyTrendCompareRequest(BaseModel):
    company_a: CompanyTrendData
    company_b: CompanyTrendData


class CompanyTrendCompareResponse(BaseModel):
    winner: str
    summary: str
    trends: Dict[str, Dict]
    confidence: str