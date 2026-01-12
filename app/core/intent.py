import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from app.actions.system import handle_system
from app.actions.web import handle_web
from app.actions.weather import handle_weather
from app.actions.email import handle_email
from app.ai.gpt import handle_gpt

df = pd.read_csv("data/os_dataset.csv")
vectorizer = CountVectorizer().fit(df["text"])

def detect_intent(user_input):
    input_vec = vectorizer.transform([user_input])
    similarities = cosine_similarity(input_vec, vectorizer.transform(df["text"]))
    idx = similarities.argmax()
    score = similarities[0][idx]

    label = df["label"][idx]

    if score < 0.5:
        return "GPT", lambda: handle_gpt(user_input)

    if "open" in label or "close" in label:
        return "SYSTEM", lambda: handle_system(label)

    if "weather" in user_input:
        return "WEATHER", lambda: handle_weather(user_input)

    if "email" in user_input:
        return "EMAIL", lambda: handle_email()

    return "GPT", lambda: handle_gpt(user_input)
