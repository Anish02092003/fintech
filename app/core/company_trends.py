def calculate_trend(values, inverse=False):
    """
    inverse=True means LOWER is better (e.g. leverage)
    """
    if len(values) < 2:
        return "insufficient data"

    start = values[0]
    end = values[-1]

    delta = end - start

    if inverse:
        delta = -delta

    if delta > 0:
        return "improving"
    elif delta < 0:
        return "deteriorating"
    else:
        return "stable"


def analyze_company_trends(company_name: str, financials: list):
    """
    financials: list of dicts (old → new)
    """

    def safe_div(a, b):
        return a / b if b else 0

    # -------------------------
    # Time series
    # -------------------------
    revenue = [f.get("revenue", 0) for f in financials]

    profit_margin = [
        safe_div(f.get("net_profit", 0), f.get("revenue", 0))
        for f in financials
    ]

    debt_ratio = [
        safe_div(f.get("total_debt", 0), f.get("total_assets", 0))
        for f in financials
    ]

    liquidity = [
        safe_div(
            f.get("current_assets", 0),
            f.get("current_liabilities", 0)
        )
        for f in financials
    ]

    # -------------------------
    # Trend classification
    # -------------------------
    trends = {
        "revenue_trend": calculate_trend(revenue),
        "profitability_trend": calculate_trend(profit_margin),
        "leverage_trend": calculate_trend(
            debt_ratio,
            inverse=True   # 👈 critical fix
        ),
        "liquidity_trend": calculate_trend(liquidity),
    }

    # -------------------------
    # Overall trend
    # -------------------------
    positives = sum(1 for v in trends.values() if v == "improving")
    negatives = sum(1 for v in trends.values() if v == "deteriorating")

    if positives >= 3:
        overall = "improving"
    elif negatives >= 3:
        overall = "deteriorating"
    else:
        overall = "mixed"

    # -------------------------
    # Graph-ready metrics
    # -------------------------
    return {
        "company": company_name,
        "overall_trend": overall,
        "trends": trends,
        "metrics": {
            "revenue": revenue,
            "profit_margin": [round(x, 3) for x in profit_margin],
            "debt_ratio": [round(x, 3) for x in debt_ratio],
            "liquidity": [round(x, 2) for x in liquidity],
        },
        "confidence": "high",
        "assumptions": [
            "Financials ordered chronologically",
            "No extraordinary one-time events"
        ],
    }