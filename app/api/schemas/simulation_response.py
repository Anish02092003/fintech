from pydantic import BaseModel
from typing import Dict, Tuple, Any


class SimulationImpact(BaseModel):
    score_delta: int
    risk_change: Tuple[str, str] | None = None


class SimulationResponse(BaseModel):
    simulation: str
    assumption: str | None = None
    before: Dict[str, Any]
    after: Dict[str, Any]
    impact: SimulationImpact