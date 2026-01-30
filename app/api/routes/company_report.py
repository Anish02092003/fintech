from fastapi import APIRouter
from app.api.schemas.company_report import (
    CompanyReportRequest,
    CompanyReportResponse
)
from app.core.company_report import generate_company_report
from app.api.schemas.company import CompanyFinancials

router = APIRouter(prefix="/company", tags=["Company Report"])


@router.post("/report", response_model=CompanyReportResponse)
def company_report(data: CompanyReportRequest):
    snapshot = CompanyFinancials(**data.snapshot)
    return generate_company_report(snapshot, data.historical)