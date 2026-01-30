from fastapi import APIRouter
from app.api.schemas.explain import ExplainRequest, ExplainResponse
from app.core.explain import generate_explanation

router = APIRouter()

@router.post("/explain", response_model=ExplainResponse)
def explain_decision(data: ExplainRequest):
    return generate_explanation(data.context, data.question)