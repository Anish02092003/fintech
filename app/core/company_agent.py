from app.core.company_finance import analyze_company_financials
from app.core.company_explain import generate_company_explanation


def run_company_agent(financials):
    # Step 1: Deterministic analysis
    analysis = analyze_company_financials(financials)

    # Step 2: Explanation layer
    explanation = generate_company_explanation(
        type("ExplainInput", (), analysis)
    )

    # Step 3: Merge results
    return {
        **analysis,
        **explanation
    }