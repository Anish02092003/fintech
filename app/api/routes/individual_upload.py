from fastapi import APIRouter, UploadFile, File, Form, HTTPException

from app.services.pdf_parser import (
    parse_financial_pdf,
    pdf_to_company_financials
)
from app.services.csv_parser import parse_financial_csv
from app.api.schemas.company import CompanyFinancials

router = APIRouter(prefix="/individual", tags=["Individual Upload"])


@router.post("/upload")
def upload_individual_file(
    name: str = Form(...),
    file: UploadFile = File(...),
    pdf_type: str = Form("summary")
):
    filename = file.filename.lower()

    # -----------------------
    # PDF Upload
    # -----------------------
    if filename.endswith(".pdf"):
        try:
            pdf_data = parse_financial_pdf(
                file.file,
                pdf_type=pdf_type
            )

            if not pdf_data or all(v == 0 for v in pdf_data.values()):
                raise HTTPException(
                    status_code=400,
                    detail="No financial data detected in PDF"
                )

            return pdf_to_company_financials(
                pdf_data=pdf_data,
                company_name=name
            )

        except HTTPException:
            raise
        except Exception as e:
            raise HTTPException(
                status_code=400,
                detail=f"Failed to parse PDF: {str(e)}"
            )

    # -----------------------
    # CSV Upload
    # -----------------------
    if filename.endswith(".csv"):
        try:
            csv_data = parse_financial_csv(file.file)
            return CompanyFinancials(
                company_name=name,
                **csv_data
            )

        except Exception:
            raise HTTPException(
                status_code=400,
                detail="Invalid CSV format"
            )

    # -----------------------
    # Unsupported File
    # -----------------------
    raise HTTPException(
        status_code=400,
        detail="Only PDF or CSV files are supported"
    )
