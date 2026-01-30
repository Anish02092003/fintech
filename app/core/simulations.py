from copy import deepcopy
from app.core.scoring import calculate_health_score
from app.core.explain import generate_explanation


def simulate_emi_change(profile, new_emi: float):
    before = calculate_health_score(profile)

    simulated = deepcopy(profile)
    simulated.emi = new_emi

    after = calculate_health_score(simulated)

    impact = {
        "score_delta": after["score"] - before["score"],
        "risk_change": [before["risk_level"], after["risk_level"]]
    }

    explanation = generate_explanation(
        context={
            "simulation": "emi_change",
            "params": {
                "old_emi": profile.emi,
                "new_emi": new_emi
            },
            "before": before,
            "after": after,
            "impact": impact
        },
        question="Explain the impact of EMI change on financial health"
    )

    return {
        "simulation": "emi_change",
        "params": {
            "old_emi": profile.emi,
            "new_emi": new_emi
        },
        "before": before,
        "after": after,
        "impact": impact,
        "explanation": explanation
    }


def simulate_income_drop(profile, drop_percent: float, months: int = 1):
    before = calculate_health_score(profile)

    simulated = deepcopy(profile)
    simulated.monthly_income *= (1 - drop_percent / 100)

    after = calculate_health_score(simulated)

    impact = {
        "score_delta": after["score"] - before["score"],
        "risk_change": [before["risk_level"], after["risk_level"]]
    }

    explanation = generate_explanation(
        context={
            "simulation": "income_drop",
            "params": {
                "drop_percent": drop_percent,
                "duration_months": months
            },
            "before": before,
            "after": after,
            "impact": impact
        },
        question="Explain the impact of income reduction on financial health"
    )

    return {
        "simulation": "income_drop",
        "params": {
            "drop_percent": drop_percent,
            "duration_months": months
        },
        "before": before,
        "after": after,
        "impact": impact,
        "explanation": explanation
    }


def simulate_expense_cut(profile, reduction_percent: float):
    # Explicit check (0.0 is valid, None is not)
    if profile.monthly_spend_mean is None:
        return {
            "error": "Transaction data required for expense-based simulation"
        }

    before = calculate_health_score(profile)

    simulated = deepcopy(profile)
    simulated.monthly_spend_mean *= (1 - reduction_percent / 100)

    after = calculate_health_score(simulated)

    impact = {
        "score_delta": after["score"] - before["score"]
    }

    explanation = generate_explanation(
        context={
            "simulation": "expense_cut",
            "params": {
                "reduction_percent": reduction_percent
            },
            "before": before,
            "after": after,
            "impact": impact
        },
        question="Explain the impact of expense reduction on financial health"
    )

    return {
        "simulation": "expense_cut",
        "params": {
            "reduction_percent": reduction_percent
        },
        "before": before,
        "after": after,
        "impact": impact,
        "explanation": explanation
    }