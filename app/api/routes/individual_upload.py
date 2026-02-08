from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from app.services.pdf_parser import parse_financial_pdf
from app.core.individual_finance import analyze_individual_financials

router = APIRouter(prefix="/individual", tags=["Individual Upload"])


@router.post("/upload")
def upload_individual_pdf(
    file: UploadFile = File(...),
    name: str = Form("User"),   # optional display name
    pdf_type: str = Form("summary")
):
    try:
        # Parse PDF
        pdf_data = parse_financial_pdf(
            file.file,
            pdf_type=pdf_type
        )

        # Analyze financial profile
        analysis = analyze_individual_financials(pdf_data)

        # Return combined response
        return {
            "name": name,
            **analysis
        }

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
