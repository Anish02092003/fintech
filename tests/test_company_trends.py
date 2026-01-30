from app.core.company_trends import analyze_company_trends


def test_company_trend_improving():
    financials = [
        {"revenue": 800, "net_profit": 60, "total_debt": 900, "total_assets": 1500, "current_assets": 400, "current_liabilities": 500},
        {"revenue": 900, "net_profit": 90, "total_debt": 700, "total_assets": 1600, "current_assets": 500, "current_liabilities": 450},
        {"revenue": 1000, "net_profit": 130, "total_debt": 500, "total_assets": 1800, "current_assets": 600, "current_liabilities": 400},
    ]

    result = analyze_company_trends("Alpha", financials)

    assert result["overall_trend"] == "improving"
    assert result["trends"]["revenue_trend"] == "improving"