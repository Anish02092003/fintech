from fastapi import APIRouter
from app.api.schemas.company_trend_compare import (
    CompanyTrendCompareRequest,
    CompanyTrendCompareResponse
)
from app.core.company_trend_compare import compare_company_trends

router = APIRouter(prefix="/company", tags=["Company Trend Comparison"])


@router.post("/compare-trends", response_model=CompanyTrendCompareResponse)
def compare_trends(data: CompanyTrendCompareRequest):
    return compare_company_trends(data.company_a, data.company_b)