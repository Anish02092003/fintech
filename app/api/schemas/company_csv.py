from pydantic import BaseModel
from typing import List, Dict


class CompanyYearData(BaseModel):
    year: int
    revenue: float
    net_profit: float
    total_assets: float
    total_liabilities: float
    total_equity: float
    current_assets: float
    current_liabilities: float
    total_debt: float


class CompanyCSVAnalysisResponse(BaseModel):
    company: str
    snapshot: Dict
    trends: Dict
    ratios: Dict
    confidence: str