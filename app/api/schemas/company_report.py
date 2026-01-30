from pydantic import BaseModel
from typing import Dict, List


class CompanyReportRequest(BaseModel):
    snapshot: Dict
    historical: List[Dict]


class CompanyReportResponse(BaseModel):
    company: str
    overall_assessment: str
    snapshot: Dict
    trends: Dict
    risk_signals: List[str]
    confidence: str
    assumptions: List[str]