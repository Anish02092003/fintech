from fastapi import APIRouter
from app.api.schemas.company_compare import (
    CompanyCompareRequest,
    CompanyCompareResponse
)
from app.core.company_compare import compare_companies
from app.api.schemas.company import CompanyFinancials

router = APIRouter(prefix="/company", tags=["Company Comparison"])


@router.post("/compare", response_model=CompanyCompareResponse)
def compare(data: CompanyCompareRequest):
    company_a = CompanyFinancials(**data.company_a)
    company_b = CompanyFinancials(**data.company_b)

    return compare_companies(company_a, company_b)