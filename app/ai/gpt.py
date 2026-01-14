import os

try:
    from openai import OpenAI
except ImportError:
    OpenAI = None


def handle_gpt(user_input: str) -> str:
    api_key = os.getenv("OPENAI_API_KEY")

    # If no API key, fail gracefully (VERY IMPORTANT FOR EXAMS)
    if not api_key or OpenAI is None:
        return "GPT service is not configured, but Jarvis is running normally."

    try:
        client = OpenAI(api_key=api_key)

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are Jarvis, a helpful AI assistant."},
                {"role": "user", "content": user_input}
            ]
        )

        return response.choices[0].message.content.strip()

    except Exception:
        return "I am having trouble thinking right now."
