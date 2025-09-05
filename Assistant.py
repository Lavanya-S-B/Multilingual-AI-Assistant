import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import google.generativeai as genai

# 🔑 Configure Gemini API
genai.configure(api_key="AIzaSyB3lbroP-fbcOr9A1gHGUOmkW34ccW6zbI")  # Replace with your API key
model = genai.GenerativeModel("gemini-1.5-flash")

# 🎤 Recognizer & TTS
recognizer = sr.Recognizer()
engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)  # Default English voice
engine.setProperty("rate", 185)

def speak(text, lang="en"):
    """Speak and print assistant message."""
    print(f"Assistant ({lang}): {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen and detect language."""
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Listening....")
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
        return response.text if response and response.text else "I couldn’t find an answer."
    except Exception as e:
        print(f"Gemini error: {e}")
        return "Sorry, my brain is offline."

def greet_user():
    """Simple greeting based on time."""
    hour = datetime.datetime.now().hour
    if hour < 12:
        return "Good morning!"
    elif hour < 18:
        return "Good afternoon!"
    else:
        return "Good evening!"

def main():
    speak("Hello! I am your friendly AI Assistant. You can ask me anything.", "en")
    speak(greet_user(), "en")

    while True:
        query, lang = listen()
        if not query:
            continue

        print(f"User ({lang}): {query}")  # Display user query
        query_lower = query.lower()

        if any(word in query_lower for word in ["exit", "quit", "bye", "stop"]):
            speak("It was nice talking to you. Goodbye!", lang)
            break

        elif "open youtube" in query_lower:
            speak("Opening YouTube", lang)
            webbrowser.open("https://youtube.com")

        elif "open google" in query_lower:
            speak("Opening Google", lang)
            webbrowser.open("https://google.com")

        elif "open instagram" in query_lower:
            speak("Opening Instagram", lang)
            webbrowser.open("https://instagram.com")

        elif "time" in query_lower:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}", lang)

        else:
            answer = ask_gemini(query, lang)
            speak(answer, lang)

if __name__ == "__main__":
    main()
