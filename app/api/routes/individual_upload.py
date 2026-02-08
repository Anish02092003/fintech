from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.services.pdf_parser import parse_financial_pdf
from app.core.individual_finance import analyze_individual_financials

router = APIRouter(prefix="/individual", tags=["Individual Upload"])


@router.post("/upload")
def upload_individual_pdf(
    file: UploadFile = File(...),
    name: str = Form(...),
    pdf_type: str = Form("summary")   # ✅ ADD THIS
):
    try:
        pdf_data = parse_financial_pdf(
            file.file,
            pdf_type=pdf_type        # ✅ PASS IT
        )

        result = analyze_individual_financials(
            pdf_data,
            name=name
        )

        return result

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
