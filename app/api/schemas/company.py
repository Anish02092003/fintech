from pydantic import BaseModel
from typing import Optional



class CompanyFinancials(BaseModel):
    company_name: str

    # Income Statement
    revenue: float
    operating_profit: float
    net_profit: float

    # Balance Sheet
    total_assets: float
    total_liabilities: float
    total_equity: float

    # Liquidity
    current_assets: float
    current_liabilities: float

    # Debt
    total_debt: float
    interest_expense: Optional[float] = None


from typing import List, Dict


class CompanyAnalysisResponse(BaseModel):
    company: str
    overall_health: str
    scores: Dict[str, str]
    key_signals: List[str]
    confidence: str