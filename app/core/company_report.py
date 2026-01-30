from app.core.company_finance import analyze_company_financials
from app.core.company_trends import analyze_company_trends


def generate_company_report(snapshot_data, historical_data):
    snapshot = analyze_company_financials(snapshot_data)
    trends = analyze_company_trends(
        snapshot_data.company_name, historical_data
    )

    risks = []
    for k, v in snapshot["scores"].items():
        if v in ["weak", "high risk"]:
            risks.append(f"{k.replace('_', ' ').title()} concern")

    summary = (
        f"{snapshot['company']} shows {snapshot['overall_health']} current health "
        f"with {trends['overall_trend']} long-term trends."
    )

    return {
        "company": snapshot["company"],
        "overall_assessment": summary,
        "snapshot": snapshot,
        "trends": trends,
        "risk_signals": risks,
        "confidence": "high",
        "assumptions": [
            "Financial data is accurate",
            "Historical data spans multiple years"
        ]
    }