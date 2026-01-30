from fastapi import APIRouter
from app.api.schemas.company import CompanyFinancials
from app.api.schemas.company_agent import CompanyAgentResponse
from app.core.company_agent import run_company_agent

router = APIRouter(prefix="/company", tags=["Company Agent"])


@router.post("/agent-analyze", response_model=CompanyAgentResponse)
def company_agent(financials: CompanyFinancials):
    return run_company_agent(financials)