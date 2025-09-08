<<<<<<< HEAD:Assistant.py

=======
import os
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import random
from dotenv import load_dotenv
import google.generativeai as genai

#  Load API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

#  Recognizer & TTS
recognizer = sr.Recognizer()
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # Default English voice
engine.setProperty("rate", 185)

# Small talk responses
small_talk = {
    "how are you": [
        "I'm doing great, thank you!",
        "I'm fine! How about you?",
        "Feeling fantastic and ready to assist!"
    ],
    "hello": ["Hello there!", "Hi! How can I help you?", "Hey!"],
    "hi": ["Hi!", "Hello!", "Hey!"],
    "tell me a joke": [
        "Why did the computer show up at work late? It had a hard drive!",
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why did the AI cross the road? To optimize its path!"
    ]
}

def speak(text, lang="en"):
    """Speak and print assistant message."""
    print(f"Assistant ({lang}): {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen and detect language."""
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print(" Listening...")
        try:
            audio = recognizer.listen(source, timeout=4, phrase_time_limit=6)

            # Try English
            try:
                query = recognizer.recognize_google(audio, language="en-IN")
                return query, "en"
            except:
                pass

            # Try Tamil
            try:
                query = recognizer.recognize_google(audio, language="ta-IN")
                return query, "ta"
            except:
                pass

            # Try Hindi
            try:
                query = recognizer.recognize_google(audio, language="hi-IN")
                return query, "hi"
            except:
                pass

            return "", "en"

        except:
            return "", "en"

def ask_gemini(question, lang="en"):
    """Ask Gemini and get short answers."""
    try:
        prompt = f"Answer briefly in {lang}: {question}"
        response = model.generate_content(prompt)
        return response.text if response and response.text else None
    except Exception as e:
        print(f"Gemini error: {e}")
        return None

def greet_user():
    """Simple greeting based on time."""
    hour = datetime.datetime.now().hour
    if hour < 12:
        return "Good morning!"
    elif hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"

def get_small_talk_response(query):
    """Check for small talk locally."""
    query_lower = query.lower()
    for key in small_talk:
        if key in query_lower:
            return random.choice(small_talk[key])
    return None

def main():
    speak("Hello! I am your friendly AI Assistant. You can ask me anything.", "en")
    speak(greet_user(), "en")

    while True:
        query, lang = listen()
        if not query:
            continue

        print(f"User ({lang}): {query}")  # Display user query
        query_lower = query.lower()

        # Exit phrases
        if any(word in query_lower for word in ["exit", "quit", "bye", "stop"]):
            speak("It was nice talking to you. Goodbye!", lang)
            break

        # Open websites
        elif "open youtube" in query_lower:
            speak("Opening YouTube", lang)
            webbrowser.open("https://youtube.com")

        elif "open google" in query_lower:
            speak("Opening Google", lang)
            webbrowser.open("https://google.com")

        elif "open instagram" in query_lower:
            speak("Opening Instagram", lang)
            webbrowser.open("https://instagram.com")

        # Time query
        elif "time" in query_lower:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}", lang)

        # Small talk locally
        else:
            response = get_small_talk_response(query)
            if response:
                speak(response, lang)
            else:
                # Ask Gemini for other queries
                answer = ask_gemini(query, lang)
                if answer:
                    speak(answer, lang)
                else:
                    # Fallback if Gemini fails
                    speak("Sorry, I cannot answer right now, but I am happy to chat!", lang)

if __name__ == "__main__":
    main()
>>>>>>> d010db8 (Remove unwanted file):VoiceAssistant.py
