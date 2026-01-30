from pydantic import BaseModel, Field
from typing import Optional


class UserProfile(BaseModel):
    age: int = Field(..., gt=0, description="User age must be positive")

    monthly_income: float = Field(
        ...,
        gt=0,
        description="Monthly income must be greater than zero"
    )

    fixed_expenses: float = Field(
        ...,
        ge=0,
        description="Fixed expenses cannot be negative"
    )

    emi: float = Field(
        ...,
        ge=0,
        description="EMI cannot be negative"
    )

    savings: Optional[float] = Field(
        0,
        ge=0,
        description="Savings cannot be negative"
    )

    # Optional – populated only if transaction CSV is uploaded
    monthly_spend_mean: Optional[float] = Field(
        None,
        ge=0,
        description="Average monthly spending"
    )

    monthly_spend_std: Optional[float] = Field(
        None,
        ge=0,
        description="Monthly spending volatility"
    )