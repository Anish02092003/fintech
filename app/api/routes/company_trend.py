from fastapi import APIRouter
from app.api.schemas.company_trend import (
    CompanyTrendRequest,
    CompanyTrendResponse
)
from app.core.company_trends import analyze_company_trends

router = APIRouter(prefix="/company", tags=["Company Trends"])


@router.post("/trend", response_model=CompanyTrendResponse)
def company_trend(data: CompanyTrendRequest):
    return analyze_company_trends(data.company, data.financials)