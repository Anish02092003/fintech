def analyze_company_financials(data):
    """
    Deterministic company financial analysis.
    No AI. No guessing. Safe math only.
    """

    signals = []
    scores = {}

    # -------------------------
    # Safety helpers
    # -------------------------
    def safe_div(numerator, denominator):
        return numerator / denominator if denominator else 0

    # -------------------------
    # Profitability
    # -------------------------
    net_margin = safe_div(data.net_profit, data.revenue)
    operating_margin = safe_div(
        getattr(data, "operating_profit", 0),
        data.revenue
    )

    if net_margin >= 0.15:
        scores["profitability"] = "good"
    elif net_margin >= 0.05:
        scores["profitability"] = "moderate"
        signals.append("Thin net profit margin")
    else:
        scores["profitability"] = "weak"
        signals.append("Low or negative profitability")

    if operating_margin < 0.10:
        signals.append("Weak operating efficiency")

    # -------------------------
    # Liquidity
    # -------------------------
    current_ratio = safe_div(
        data.current_assets,
        data.current_liabilities
    )

    if current_ratio >= 1.5:
        scores["liquidity"] = "strong"
    elif current_ratio >= 1.0:
        scores["liquidity"] = "adequate"
        signals.append("Tight short-term liquidity")
    else:
        scores["liquidity"] = "weak"
        signals.append("Insufficient short-term liquidity")

    # -------------------------
    # Leverage
    # -------------------------
    total_equity = getattr(data, "total_equity", None)

    if not total_equity or total_equity <= 0:
        scores["leverage"] = "high risk"
        signals.append("Negative or missing equity")
        debt_equity = None
    else:
        debt_equity = safe_div(data.total_debt, total_equity)

        if debt_equity <= 0.5:
            scores["leverage"] = "low risk"
        elif debt_equity <= 1.0:
            scores["leverage"] = "moderate risk"
            signals.append("Elevated leverage")
        else:
            scores["leverage"] = "high risk"
            signals.append("High debt relative to equity")

    # -------------------------
    # Overall Health
    # -------------------------
    weak_flags = sum(
        1 for v in scores.values()
        if v in ["weak", "high risk"]
    )

    if weak_flags >= 2:
        overall = "weak"
    elif weak_flags == 1:
        overall = "moderate"
    else:
        overall = "strong"

    return {
        "company": data.company_name,
        "overall_health": overall,
        "scores": scores,
        "key_signals": list(set(signals)),
        "metrics": {
            "net_margin": round(net_margin, 3),
            "operating_margin": round(operating_margin, 3),
            "current_ratio": round(current_ratio, 2),
            "debt_to_equity": round(debt_equity, 2)
            if debt_equity is not None else None
        },
        "confidence": "high"
    }