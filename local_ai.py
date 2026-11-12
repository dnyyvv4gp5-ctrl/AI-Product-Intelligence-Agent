import json
import urllib.request
import urllib.error

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "qwen2.5:1.5b"

def analyse_feedback(feedback):
    prompt = f"""
    You are an AI product analyst.
    Analyse this customer feedback:

    {feedback}

    Return:
    1. Customer problem
    2. Sentiment
    3. Urgency (Low, Medium, High)
    4. Suggested product improvement
    5. Business impact
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
        with urllib.request.urlopen(request, timeout=120) as response:
            result = json.loads(response.read())
            return result["response"]
    except Exception as error:
        return f"AI analysis failed: {error}"
