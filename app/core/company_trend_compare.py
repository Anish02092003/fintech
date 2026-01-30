from app.core.company_trends import analyze_company_trends


def compare_company_trends(company_a, company_b):
    """
    Compares long-term financial trends of two companies.
    Deterministic, explainable, graph-friendly.
    Supports both dict-based and object-based inputs.
    """

    # -------------------------
    # Input normalization
    # -------------------------
    name_a = company_a["company"] if isinstance(company_a, dict) else company_a.company
    fin_a  = company_a["financials"] if isinstance(company_a, dict) else company_a.financials

    name_b = company_b["company"] if isinstance(company_b, dict) else company_b.company
    fin_b  = company_b["financials"] if isinstance(company_b, dict) else company_b.financials

    trend_a = analyze_company_trends(name_a, fin_a)
    trend_b = analyze_company_trends(name_b, fin_b)

    # -------------------------
    # Overall trend scoring
    # -------------------------
    overall_score_map = {
        "improving": 2,
        "mixed": 1,
        "stable": 1,
        "deteriorating": 0,
    }

    score_a = overall_score_map.get(trend_a["overall_trend"], 1)
    score_b = overall_score_map.get(trend_b["overall_trend"], 1)

    # -------------------------
    # Tie-breaker: trend details
    # -------------------------
    def trend_detail_score(trends: dict) -> int:
        detail_map = {
            "improving": 1,
            "stable": 0,
            "mixed": 0,
            "deteriorating": -1,
        }
        return sum(detail_map.get(v, 0) for v in trends.values())

    # -------------------------
    # Winner logic
    # -------------------------
    if score_a == score_b:
        detail_a = trend_detail_score(trend_a["trends"])
        detail_b = trend_detail_score(trend_b["trends"])

        if detail_a > detail_b:
            winner = trend_a["company"]
        elif detail_b > detail_a:
            winner = trend_b["company"]
        else:
            winner = "tie"
    else:
        winner = trend_a["company"] if score_a > score_b else trend_b["company"]

    # -------------------------
    # Summary
    # -------------------------
    summary = (
        f"{winner} shows stronger long-term financial trends."
        if winner != "tie"
        else "Both companies show similar long-term financial trends."
    )

    # -------------------------
    # Final output
    # -------------------------
    return {
        "winner": winner,
        "summary": summary,
        "overall_trends": {
            trend_a["company"]: trend_a["overall_trend"],
            trend_b["company"]: trend_b["overall_trend"],
        },
        "trend_breakdown": {
            trend_a["company"]: trend_a["trends"],
            trend_b["company"]: trend_b["trends"],
        },
        "metrics": {
            trend_a["company"]: trend_a["metrics"],
            trend_b["company"]: trend_b["metrics"],
        },
        "confidence": "high",
        "assumptions": [
            "Historical financials are chronologically ordered",
            "No extraordinary one-time events",
        ],
    }