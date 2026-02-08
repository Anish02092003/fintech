from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.api.schemas.simulation import SimulationResponse
from app.api.schemas.simulation_request import SimulationRequest
from app.api.schemas.error import ErrorResponse

from app.core.simulations import (
    simulate_emi_change,
    simulate_income_drop,
    simulate_expense_cut
)

from app.core.individual_finance import analyze_individual_financials


router = APIRouter(prefix="/simulate", tags=["Simulations"])


# =====================================================
# EXISTING ADVANCED SIMULATION (UNCHANGED)
# =====================================================

@router.post(
    "/",
    response_model=SimulationResponse,
    responses={400: {"model": ErrorResponse}}
)
def run_simulation(data: SimulationRequest):

    if data.type == "emi_change":
        if not data.emi_params:
            raise HTTPException(
                status_code=400,
                detail="emi_params required for emi_change simulation"
            )
        return simulate_emi_change(
            data.profile,
            data.emi_params.new_emi
        )

    if data.type == "income_drop":
        if not data.income_params:
            raise HTTPException(
                status_code=400,
                detail="income_params required for income_drop simulation"
            )
        return simulate_income_drop(
            data.profile,
            data.income_params.drop_percent,
            data.income_params.months
        )

    if data.type == "expense_cut":
        if not data.expense_params:
            raise HTTPException(
                status_code=400,
                detail="expense_params required for expense_cut simulation"
            )
        result = simulate_expense_cut(
            data.profile,
            data.expense_params.reduction_percent
        )

        if "error" in result:
            raise HTTPException(status_code=400, detail=result["error"])

        return result

    raise HTTPException(status_code=400, detail="Unknown simulation type")


# =====================================================
# NEW: QUICK SIMULATION (FOR FRONTEND SLIDERS)
# =====================================================

class QuickSimulationRequest(BaseModel):
    income: float
    expenses: float
    savings: float
    debt: float


@router.post("/quick")
def quick_simulation(data: QuickSimulationRequest):
    """
    Lightweight simulation for UI sliders
    """

    # Build a profile compatible with your finance engine
    profile = {
        "income": data.income,
        "expenses": data.expenses,
        "savings": data.savings,
        "debt": data.debt,
    }

    # Reuse existing health analysis
    result = analyze_individual_financials(profile)

    return {
        "overall_health": result["overall_health"],
        "scores": result["scores"],
        "metrics": profile,
        "confidence": "medium",
        "notes": [
            "Simulation based on adjusted user inputs",
            "No historical effects applied"
        ]
    }
