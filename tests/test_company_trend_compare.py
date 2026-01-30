from app.core.company_trend_compare import compare_company_trends


def test_trend_comparison():
    company_a = {
        "company": "Alpha",
        "financials": [
            {"revenue": 800}, {"revenue": 1000}
        ]
    }

    company_b = {
        "company": "Beta",
        "financials": [
            {"revenue": 1000}, {"revenue": 900}
        ]
    }

    result = compare_company_trends(company_a, company_b)

    assert result["winner"] == "Alpha"