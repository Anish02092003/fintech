from app.services.llm import run_llm


def generate_explanation(context: dict, question: str) -> dict:
    """
    Hybrid explanation engine:
    1) Always generate a deterministic explanation
    2) Enhance with local LLM if available
    """

    # -------------------------
    # Rule-based baseline
    # -------------------------
    score_delta = context.get("impact", {}).get("score_delta", 0)

    if score_delta < 0:
        base_explanation = (
            "Your financial score decreased because increased obligations "
            "reduced your disposable income and savings capacity."
        )
        confidence = "high"
    elif score_delta > 0:
        base_explanation = (
            "Your financial score improved due to better disposable income "
            "and reduced financial stress."
        )
        confidence = "medium"
    else:
        base_explanation = (
            "Your financial score remained stable as the changes had a neutral impact."
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
- Do NOT provide financial advice
- ONLY explain based on the given data

Context:
{context}

Question:
{question}

Base explanation:
{base_explanation}

Enhance the explanation with clearer reasoning in plain English.
"""

        llm_explanation = run_llm(prompt).strip()

        return {
            "explanation": llm_explanation,
            "confidence": confidence,
            "assumptions": [
                "Input data is accurate",
                "No external financial factors considered"
            ],
            "source": "rule + local LLM"
        }

    except Exception:
        # -------------------------
        # Safe fallback
        # -------------------------
        return {
            "explanation": base_explanation,
            "confidence": confidence,
            "assumptions": [
                "Input data is accurate",
                "LLM unavailable, rule-based explanation used"
            ],
            "source": "rule-based"
        }