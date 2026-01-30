from app.core.company_finance import analyze_company_financials
from app.api.schemas.company import CompanyFinancials


def test_company_financials_strong():
    company = CompanyFinancials(
        company_name="Alpha",
        revenue=1000,
        net_profit=200,
        operating_profit=180,
        total_assets=2000,
        total_liabilities=800,
        total_debt=300,
        total_equity=1200,
        current_assets=600,
        current_liabilities=300,
    )

    result = analyze_company_financials(company)

    assert result["overall_health"] == "strong"
    assert result["scores"]["profitability"] == "good"
    assert result["scores"]["liquidity"] == "strong"
    assert result["scores"]["leverage"] in ["low risk", "moderate risk"]