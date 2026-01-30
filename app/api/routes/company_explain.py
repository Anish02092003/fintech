from fastapi import APIRouter
from app.api.schemas.company_explain import (
    CompanyExplainRequest,
    CompanyExplainResponse
)
from app.core.company_explain import generate_company_explanation

router = APIRouter(prefix="/company", tags=["Company Explanation"])


@router.post("/explain", response_model=CompanyExplainResponse)
def explain_company(data: CompanyExplainRequest):
    return generate_company_explanation(data)