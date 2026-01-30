from fastapi import APIRouter
from app.api.schemas.company import CompanyFinancials, CompanyAnalysisResponse
from app.core.company_finance import analyze_company_financials

router = APIRouter(prefix="/company", tags=["Company Analysis"])


@router.post("/analyze", response_model=CompanyAnalysisResponse)
def analyze_company(data: CompanyFinancials):
    return analyze_company_financials(data)