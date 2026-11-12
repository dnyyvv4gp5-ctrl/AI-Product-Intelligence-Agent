import json
import urllib.request

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen2.5:1.5b"


def analyse_roadmap(roadmap_text):
    prompt = f"""
You are a senior AI Product Manager.

Analyse this product roadmap:

{roadmap_text}

Provide a structured product strategy report covering:

1. Most important customer problems
2. Why these problems matter to the business
3. Recommended product priorities and reasoning
4. Potential business risks
5. Suggested KPIs to measure success
6. Practical next steps for the Product Manager

Use clear, professional business language.
Base your analysis on the supplied roadmap. Do not invent customer data.
"""

    data = json.dumps({
        "model": MODEL,
        "prompt": prompt,
        "stream": False
    }).encode("utf-8")

    request = urllib.request.Request(
        OLLAMA_URL,
        data=data,
        headers={"Content-Type": "application/json"}
    )

    try:
        with urllib.request.urlopen(request, timeout=180) as response:
            result = json.loads(response.read())
            return result["response"]
    except Exception as error:
        return f"AI roadmap analysis failed: {error}"
