from pydantic import BaseModel
from typing import Dict, List


class CompanyCompareRequest(BaseModel):
    company_a: Dict
    company_b: Dict


class CompanyCompareResponse(BaseModel):
    winner: str
    summary: str

    comparison: Dict[str, Dict[str, str]]
    key_differences: List[str]

    confidence: str
    assumptions: List[str]