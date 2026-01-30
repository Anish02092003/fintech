def generate_company_explanation(data):
    explanation_parts = []

    explanation_parts.append(
        f"The overall financial health of {data.company} is assessed as {data.overall_health}."
    )

    for area, status in data.scores.items():
        explanation_parts.append(
            f"{area.capitalize()} performance is considered {status}."
        )

    if data.key_signals:
        explanation_parts.append(
            "Key risk signals include: " + ", ".join(data.key_signals) + "."
        )

    explanation_parts.append(
        "This assessment is based on standard financial ratios and does not account for future market conditions."
    )

    return {
        "explanation": " ".join(explanation_parts),
        "confidence": "high",
        "assumptions": [
            "Financial data is accurate and recent",
            "No extraordinary one-time events"
        ]
    }