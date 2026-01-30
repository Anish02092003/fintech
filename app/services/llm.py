import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "phi3"

def run_llm(prompt: str) -> str:
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "prompt": prompt,
            "stream": False
        },
        timeout=60
    )

    response.raise_for_status()
    return response.json()["response"]