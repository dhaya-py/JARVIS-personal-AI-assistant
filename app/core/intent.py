import os
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from app.actions.system import handle_system
from app.actions.web import handle_web
from app.actions.weather import handle_weather
from app.actions.email import handle_email
from app.ai.gpt import handle_gpt

# -------- SAFE DATA PATH RESOLUTION --------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "os_dataset.csv")

df = pd.read_csv(DATA_PATH)
vectorizer = CountVectorizer().fit(df["text"])
# ------------------------------------------


def detect_intent(user_input: str):
    text = user_input.lower()

    # Dataset-based intent
    input_vec = vectorizer.transform([text])
    similarities = cosine_similarity(input_vec, vectorizer.transform(df["text"]))
    idx = similarities.argmax()
    score = similarities[0][idx]
    label = df["label"][idx]

    if score > 0.5:
        if "open" in label or "close" in label:
            return "SYSTEM", lambda: handle_system(label)

    # Keyword-based intent
    if "weather" in text:
        return "WEATHER", lambda: handle_weather(text)

    if "email" in text:
        return "EMAIL", lambda: handle_email()

    if "search" in text or "google" in text or "http" in text:
        return "WEB", lambda: handle_web("https://www.google.com")

    # Fallback
    return "GPT", lambda: handle_gpt(text)
