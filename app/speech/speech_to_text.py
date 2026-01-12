import speech_recognition as sr

def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_google(audio).lower()
    except:
        return ""
