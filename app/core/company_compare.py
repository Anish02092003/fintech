from app.core.company_finance import analyze_company_financials
from app.core.company_rating import assign_credit_rating   # ✅ ADD THIS


def compare_companies(data_a, data_b):
    """
    Deterministic company comparison engine.
    No AI. No guessing. Fully explainable.
    """

    analysis_a = analyze_company_financials(data_a)
    analysis_b = analyze_company_financials(data_b)

    # -------------------------
    # Credit ratings (NEW)
    # -------------------------
    rating_a = assign_credit_rating(analysis_a)
    rating_b = assign_credit_rating(analysis_b)

    # -------------------------
    # Score normalization
    # -------------------------
    score_map = {
        "strong": 3,
        "good": 2,
        "adequate": 2,
        "moderate": 1,
        "weak": 0,
        "low risk": 3,
        "moderate risk": 1,
        "high risk": 0,
    }

    def numeric_score(scores: dict) -> int:
        return sum(score_map.get(v, 1) for v in scores.values())

    score_a = numeric_score(analysis_a["scores"])
    score_b = numeric_score(analysis_b["scores"])

    # -------------------------
    # Winner logic
    # -------------------------
    if score_a > score_b:
        winner = analysis_a["company"]
    elif score_b > score_a:
        winner = analysis_b["company"]
    else:
        winner = "tie"

    # -------------------------
    # Differences (human readable)
    # -------------------------
    differences = []
    for metric in analysis_a["scores"]:
        a_val = analysis_a["scores"][metric]
        b_val = analysis_b["scores"][metric]

        if a_val != b_val:
            differences.append(
                f"{metric.capitalize()}: "
                f"{analysis_a['company']} is {a_val}, "
                f"{analysis_b['company']} is {b_val}"
            )

    # -------------------------
    # Metrics (graph-ready)
    # -------------------------
    metrics_comparison = {
        analysis_a["company"]: analysis_a["metrics"],
        analysis_b["company"]: analysis_b["metrics"],
    }

    # -------------------------
    # Summary
    # -------------------------
    summary = (
        f"{winner} appears financially stronger overall based on "
        "profitability, liquidity, and leverage."
        if winner != "tie"
        else "Both companies show comparable financial strength."
    )

    # -------------------------
    # Final output
    # -------------------------
    return {
        "winner": winner,
        "summary": summary,
        "scores": {
            analysis_a["company"]: analysis_a["scores"],
            analysis_b["company"]: analysis_b["scores"],
        },
        "metrics": metrics_comparison,
        "key_differences": differences,
        "numeric_score": {
            analysis_a["company"]: score_a,
            analysis_b["company"]: score_b,
        },
        "credit_rating": {                      # ✅ NEW
            analysis_a["company"]: rating_a,
            analysis_b["company"]: rating_b,
        },
        "confidence": "high",
        "assumptions": [
            "Financial data is accurate and comparable",
            "Same fiscal period used for both companies",
        ],
    }