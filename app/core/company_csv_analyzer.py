from app.core.company_finance import analyze_company_financials
from app.core.company_trends import analyze_company_trends


def analyze_csv_financials(company_name: str, data):
    latest = data[-1].dict()
    snapshot = analyze_company_financials(latest)

    trends = analyze_company_trends(
        company_name,
        [d.dict() for d in data]
    )

    ratios = {
        "profit_margin": latest["net_profit"] / latest["revenue"],
        "current_ratio": latest["current_assets"] / latest["current_liabilities"],
        "debt_equity": latest["total_debt"] / latest["total_equity"]
    }

    return {
        "company": company_name,
        "snapshot": snapshot,
        "trends": trends,
        "ratios": ratios,
        "confidence": "high"
    }