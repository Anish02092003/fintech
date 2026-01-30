from fastapi import APIRouter, UploadFile, File
import tempfile
import os

from app.core.transactions import parse_transactions_csv, aggregate_monthly_spending

router = APIRouter()

@router.post("/transactions/upload")
async def upload_transactions(file: UploadFile = File(...)):
    if not file.filename.endswith(".csv"):
        return {"error": "Only CSV files are supported"}

    with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as tmp:
        contents = await file.read()
        tmp.write(contents)
        temp_path = tmp.name

    try:
        df = parse_transactions_csv(temp_path)
        aggregates = aggregate_monthly_spending(df)
    finally:
        os.remove(temp_path)

    return {
        "status": "success",
        "aggregates": aggregates
    }