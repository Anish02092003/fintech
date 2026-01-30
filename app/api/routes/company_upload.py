from fastapi import APIRouter, UploadFile, File, Form, HTTPException

from app.services.pdf_parser import (
    parse_financial_pdf,
    pdf_to_company_financials
)
from app.services.csv_parser import parse_financial_csv
from app.api.schemas.company import CompanyFinancials
from app.core.company_compare import compare_companies

router = APIRouter(prefix="/company", tags=["Company Upload"])


@router.post("/compare-upload")
def compare_uploaded_companies(
    file_a: UploadFile = File(...),
    file_b: UploadFile = File(...),
    company_a_name: str = Form(...),
    company_b_name: str = Form(...)
):
    def load_company(file: UploadFile, company_name: str) -> CompanyFinancials:
        filename = file.filename.lower()

        # -------- PDF --------
        if filename.endswith(".pdf"):
            try:
                pdf_data = parse_financial_pdf(file.file)
                return pdf_to_company_financials(pdf_data, company_name)
            except Exception:
                raise HTTPException(
                    status_code=400,
                    detail=f"Failed to parse PDF for {company_name}"
                )

        # -------- CSV --------
        if filename.endswith(".csv"):
            try:
                csv_data = parse_financial_csv(file.file)
                return CompanyFinancials(
                    company_name=company_name,
                    **csv_data
                )
            except Exception:
                raise HTTPException(
                    status_code=400,
                    detail=f"Invalid CSV format for {company_name}"
                )

        # -------- Unsupported --------
        raise HTTPException(
            status_code=400,
            detail="Only PDF or CSV files are supported"
        )

    company_a = load_company(file_a, company_a_name)
    company_b = load_company(file_b, company_b_name)

    return compare_companies(company_a, company_b)