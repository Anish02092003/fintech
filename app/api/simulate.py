from fastapi import APIRouter, HTTPException
from app.core.simulations import (
    simulate_emi_change,
    simulate_income_drop,
    simulate_expense_cut
)
from app.api.schemas import SimulationRequest

router = APIRouter(prefix="/simulate", tags=["Simulations"])


@router.post("/")
def run_simulation(req: SimulationRequest):
    sim_type = req.type
    params = req.params
    profile = req.profile

    try:
        if sim_type == "emi_change":
            return simulate_emi_change(
                profile,
                new_emi=params["new_emi"]
            )

        elif sim_type == "income_drop":
            return simulate_income_drop(
                profile,
                drop_percent=params["percent"],
                months=params.get("months", 1)
            )

        elif sim_type == "expense_cut":
            return simulate_expense_cut(
                profile,
                reduction_percent=params["percent"]
            )

        else:
            raise HTTPException(
                status_code=400,
                detail="Unknown simulation type"
            )

    except KeyError as e:
        raise HTTPException(
            status_code=422,
            detail=f"Missing parameter: {str(e)}"
        )