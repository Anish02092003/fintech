from app.core.company_compare import compare_companies
from app.api.schemas.company import CompanyFinancials


def test_company_comparison_winner():
    a = CompanyFinancials(
        company_name="Alpha",
        revenue=1000,
        net_profit=200,
        operating_profit=150,
        total_assets=2000,
        total_liabilities=800,
        total_debt=300,
        total_equity=1200,
        current_assets=600,
        current_liabilities=300,
    )

    b = CompanyFinancials(
        company_name="Beta",
        revenue=1000,
        net_profit=50,
        operating_profit=40,
        total_assets=2000,
        total_liabilities=1200,
        total_debt=900,
        total_equity=1300,
        current_assets=400,
        current_liabilities=500,
    )

    result = compare_companies(a, b)

    assert result["winner"] == "Alpha"
    assert "credit_rating" in result
    assert result["numeric_score"]["Alpha"] > result["numeric_score"]["Beta"]