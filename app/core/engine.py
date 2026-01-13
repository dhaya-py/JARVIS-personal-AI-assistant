from app.speech.speech_to_text import listen
from app.speech.text_to_speech import speak
from app.core.intent import detect_intent
from app.db.database import log_interaction
from app.utils.logger import log_info, log_error




class JarvisEngine:

    def __init__(self):
        self.running = True

    def start(self):
        speak("Jarvis is online")

        while self.running:
            user_input = listen()

            if not user_input:
                continue

            if user_input in ["stop", "exit", "quit"]:
                self.stop()
                break

            intent, data = detect_intent(user_input)

            response = self.handle_intent(intent, data)

            speak(response)

            log_interaction(user_input, response)

    def stop(self):
        self.running = False
        speak("Jarvis is shutting down")

    def handle_intent(self, intent, data):
        if intent == "SYSTEM":
            return data()

        elif intent == "WEB":
            return data()

        elif intent == "WEATHER":
            return data()

        elif intent == "EMAIL":
            return data()

        elif intent == "GPT":
            return data()

        else:
            return "Sorry, I did not understand that"


    def log_interaction(self, user_input, response):
        log_info(f"User said: {user_input}")
        log_info(f"Jarvis replied: {response}")