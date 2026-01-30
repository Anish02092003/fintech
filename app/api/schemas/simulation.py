from pydantic import BaseModel
from typing import Dict, List, Optional, Any


# -------------------------
# Reusable blocks
# -------------------------

class HealthScore(BaseModel):
    score: int
    risk_level: str
    accuracy: Optional[str] = None
    components: Optional[Dict[str, int]] = None
    signals: Optional[List[str]] = None


class Impact(BaseModel):
    score_delta: int
    risk_change: Optional[List[str]] = None


class Explanation(BaseModel):
    explanation: str
    confidence: str
    assumptions: List[str]
    source: Optional[str] = None


# -------------------------
# Simulation Response
# -------------------------

class SimulationResponse(BaseModel):
    simulation: str
    params: Dict[str, Any]
    before: HealthScore
    after: HealthScore
    impact: Impact
    explanation: Explanation