from fastapi import APIRouter, HTTPException
from app.api.schemas.company_explain import (
    CompanyExplainRequest,
    CompanyExplainResponse
)
from app.core.company_explain import generate_company_explanation

router = APIRouter(prefix="/company", tags=["Company Explanation"])


@router.post("/explain", response_model=CompanyExplainResponse)
def explain_company(data: CompanyExplainRequest):
    try:
        result = generate_company_explanation(data)
        return result

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Company explanation failed: {str(e)}"
        )
