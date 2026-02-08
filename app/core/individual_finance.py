def analyze_individual_financials(profile: dict):
    income = profile.get("income", 0)
    expenses = profile.get("expenses", 0)
    savings = profile.get("savings", 0)
    debt = profile.get("debt", 0)

    # Simple ratios
    savings_rate = (income - expenses) / income if income else 0
    debt_ratio = debt / savings if savings else 1

    scores = {
        "liquidity": "good" if savings_rate > 0.2 else "weak",
        "leverage": "low risk" if debt_ratio < 1 else "high risk",
    }

    if scores["liquidity"] == "good" and scores["leverage"] == "low risk":
        overall = "good"
    elif scores["liquidity"] == "weak" and scores["leverage"] == "high risk":
        overall = "poor"
    else:
        overall = "average"

    return {
        "overall_health": overall,
        "scores": scores,
    }
