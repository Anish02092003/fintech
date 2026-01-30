from fastapi import APIRouter
from app.models.profile import UserProfile
from app.core.scoring import calculate_health_score

router = APIRouter()

@router.post("/health-score")
def get_health_score(profile: UserProfile):
    return calculate_health_score(profile)