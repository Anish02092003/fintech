from fastapi import APIRouter
from app.services.llm import explain_result

router = APIRouter()

@router.post("/explain")
def explain(data: dict):
    return explain_result(data)