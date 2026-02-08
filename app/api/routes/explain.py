from fastapi import APIRouter, HTTPException
from app.api.schemas.explain import ExplainRequest, ExplainResponse
from app.core.explain import generate_explanation

router = APIRouter(prefix="/explain", tags=["Explain"])


@router.post("/", response_model=ExplainResponse)
def explain_decision(data: ExplainRequest):
    try:
        result = generate_explanation(
            context=data.context,
            question=data.question
        )
        return result

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Explanation generation failed: {str(e)}"
        )
