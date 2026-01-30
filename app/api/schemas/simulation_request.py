from pydantic import BaseModel, Field
from typing import Literal, Optional
from app.models.profile import UserProfile


# -------------------------
# Parameter Schemas
# -------------------------

class EmiChangeParams(BaseModel):
    new_emi: float = Field(..., gt=0)


class IncomeDropParams(BaseModel):
    drop_percent: float = Field(..., gt=0, le=100)
    months: Optional[int] = Field(1, gt=0)


class ExpenseCutParams(BaseModel):
    reduction_percent: float = Field(..., gt=0, le=100)


# -------------------------
# Main Request Schema
# -------------------------

class SimulationRequest(BaseModel):
    type: Literal["emi_change", "income_drop", "expense_cut"]
    profile: UserProfile

    # one of these will be used depending on type
    emi_params: Optional[EmiChangeParams] = None
    income_params: Optional[IncomeDropParams] = None
    expense_params: Optional[ExpenseCutParams] = None