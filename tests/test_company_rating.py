from app.core.company_rating import assign_credit_rating


def test_credit_rating_strong():
    analysis = {
        "overall_health": "strong",
        "scores": {
            "profitability": "good",
            "liquidity": "strong",
            "leverage": "low risk",
        },
        "metrics": {},
    }

    rating = assign_credit_rating(analysis)
    assert rating in ["AAA", "AA"]