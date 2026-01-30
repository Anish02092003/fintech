# app/core/company_rating.py

def assign_credit_rating(analysis: dict) -> str:
    """
    Deterministic credit-style rating.
    """

    scores = analysis["scores"]
    metrics = analysis["metrics"]

    risk_flags = sum(
        1 for v in scores.values()
        if v in ["weak", "high risk"]
    )

    if analysis["overall_health"] == "strong" and risk_flags == 0:
        return "AAA"
    if analysis["overall_health"] == "strong":
        return "AA"
    if analysis["overall_health"] == "moderate":
        return "A"
    if analysis["overall_health"] == "weak":
        return "BBB"

    return "BB"