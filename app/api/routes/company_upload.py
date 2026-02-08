from fastapi import APIRouter, UploadFile, File, Form, HTTPException

from app.services.pdf_parser import parse_financial_pdf, pdf_to_company_financials
from app.services.csv_parser import parse_financial_csv
from app.api.schemas.company import CompanyFinancials
from app.core.company_compare import compare_companies

router = APIRouter(prefix="/company", tags=["Company Upload"])


# =====================================================
# SINGLE COMPANY UPLOAD
# =====================================================
@router.post("/upload")
def upload_single_company(
    company_name: str = Form(...),
    file: UploadFile = File(...),
    pdf_type: str = Form("summary"),
):
    filename = file.filename.lower()

    try:
        if filename.endswith(".pdf"):
            pdf_data = parse_financial_pdf(file.file, pdf_type=pdf_type)
            return pdf_to_company_financials(pdf_data, company_name)

        if filename.endswith(".csv"):
            csv_data = parse_financial_csv(file.file)
            return CompanyFinancials(company_name=company_name, **csv_data)

        raise HTTPException(status_code=400, detail="Unsupported file type")

    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# =====================================================
# TWO COMPANY COMPARE UPLOAD
# =====================================================
@router.post("/compare-upload")
def compare_uploaded_companies(
    company_a_name: str = Form(...),
    company_b_name: str = Form(...),
    file_a: UploadFile = File(...),
    file_b: UploadFile = File(...),
    pdf_type: str = Form("summary"),
):
    def load_company(file: UploadFile, name: str) -> CompanyFinancials:
        filename = file.filename.lower()

        if filename.endswith(".pdf"):
            pdf_data = parse_financial_pdf(file.file, pdf_type=pdf_type)
            return pdf_to_company_financials(pdf_data, name)

        if filename.endswith(".csv"):
            csv_data = parse_financial_csv(file.file)
            return CompanyFinancials(company_name=name, **csv_data)

        raise HTTPException(status_code=400, detail="Unsupported file type")

    company_a = load_company(file_a, company_a_name)
    company_b = load_company(file_b, company_b_name)

    return compare_companies(company_a, company_b)
