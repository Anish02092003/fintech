def calculate_savings_health(income, fixed_expenses, emi):
    if income <= 0:
        return 0, "invalid income"

    savings_rate = (income - fixed_expenses - emi) / income

    if savings_rate >= 0.30:
        return 30, "healthy savings rate"
    elif savings_rate >= 0.20:
        return 24, "decent savings rate"
    elif savings_rate >= 0.10:
        return 18, "low savings rate"
    elif savings_rate >= 0.05:
        return 10, "very low savings rate"
    else:
        return 5, "critical savings rate"


def calculate_debt_stress(income, emi):
    if income <= 0:
        return 0, "invalid income"

    dti = emi / income

    if dti <= 0.20:
        return 30, "low debt burden"
    elif dti <= 0.30:
        return 24, "manageable debt"
    elif dti <= 0.40:
        return 18, "elevated debt risk"
    elif dti <= 0.50:
        return 10, "high debt risk"
    else:
        return 5, "critical debt burden"


def calculate_emergency_buffer(savings, fixed_expenses):
    if fixed_expenses <= 0:
        return 20, "no fixed expenses"

    months = savings / fixed_expenses

    if months >= 6:
        return 20, "strong emergency buffer"
    elif months >= 3:
        return 15, "adequate emergency buffer"
    elif months >= 1:
        return 8, "weak emergency buffer"
    else:
        return 3, "no emergency buffer"


def calculate_expense_stability(mean, std):
    if mean is None or mean <= 0:
        return 0, "insufficient spending data"

    if std is None or std < 0:
        return 0, "invalid spending data"

    volatility = std / mean

    if volatility <= 0.10:
        return 20, "very stable spending"
    elif volatility <= 0.20:
        return 15, "moderately stable spending"
    elif volatility <= 0.30:
        return 8, "unstable spending"
    else:
        return 3, "highly volatile spending"


def calculate_health_score(profile):
    components = {}
    signals = []

    # --- Core components ---
    savings_score, savings_msg = calculate_savings_health(
        profile.monthly_income,
        profile.fixed_expenses,
        profile.emi
    )
    components["savings_health"] = savings_score
    signals.append(savings_msg)

    debt_score, debt_msg = calculate_debt_stress(
        profile.monthly_income,
        profile.emi
    )
    components["debt_stress"] = debt_score
    signals.append(debt_msg)

    buffer_score, buffer_msg = calculate_emergency_buffer(
        profile.savings or 0,
        profile.fixed_expenses
    )
    components["emergency_buffer"] = buffer_score
    signals.append(buffer_msg)

    # --- Optional transaction-based component ---
    max_score = 80
    accuracy = "low"

    if profile.monthly_spend_mean is not None and profile.monthly_spend_std is not None:
        stability_score, stability_msg = calculate_expense_stability(
            profile.monthly_spend_mean,
            profile.monthly_spend_std
        )
        components["expense_stability"] = stability_score
        signals.append(stability_msg)
        max_score = 100
        accuracy = "high"

    raw_score = sum(components.values())
    final_score = round((raw_score / max_score) * 100)

    # --- Risk bucket ---
    if final_score >= 75:
        risk = "low"
    elif final_score >= 50:
        risk = "moderate"
    else:
        risk = "high"

    return {
        "score": final_score,
        "risk_level": risk,
        "accuracy": accuracy,
        "components": components,
        "signals": list(set(signals))
    }