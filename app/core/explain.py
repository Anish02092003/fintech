from app.services.llm import run_llm


def generate_explanation(context: dict, question: str | None = None) -> dict:
    """
    Hybrid explanation engine:
    1) Deterministic explanation (always works)
    2) Optional LLM enhancement
    """

    context = context or {}
    question = question or "Explain the financial result."

    # -------------------------
    # Safe extraction
    # -------------------------
    impact = context.get("impact", {}) or {}
    score_delta = impact.get("score_delta", 0)

    # -------------------------
    # Rule-based explanation
    # -------------------------
    if score_delta < 0:
        base_explanation = (
            "The financial score decreased because higher obligations "
            "reduced disposable income and savings capacity."
        )
        confidence = "high"

    elif score_delta > 0:
        base_explanation = (
            "The financial score improved due to stronger income balance "
            "and lower financial stress."
        )
        confidence = "medium"

    else:
        base_explanation = (
            "The financial score remained stable because the financial "
            "changes had minimal impact."
        )
        confidence = "medium"

    # -------------------------
    # LLM enhancement (optional)
    # -------------------------
    try:
        prompt = f"""
You are a financial analyst assistant.

Rules:
- Do NOT invent numbers
- Do NOT give financial advice
- Explain clearly and simply

Context:
{context}

Question:
{question}

Base explanation:
{base_explanation}

Rewrite the explanation in clearer plain English.
"""

        llm_explanation = run_llm(prompt)

        if llm_explanation and isinstance(llm_explanation, str):
            return {
                "explanation": llm_explanation.strip(),
                "confidence": confidence,
                "assumptions": [
                    "Input data is accurate",
                    "Explanation enhanced using local LLM"
                ],
                "source": "rule + LLM"
            }

    except Exception:
        pass

    # -------------------------
    # Safe fallback
    # -------------------------
    return {
        "explanation": base_explanation,
        "confidence": confidence,
        "assumptions": [
            "Input data is accurate",
            "Rule-based explanation used"
        ],
        "source": "rule-based"
    }
