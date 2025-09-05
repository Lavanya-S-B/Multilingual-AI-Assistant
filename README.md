🌐 Multilingual AI Assistant

A smart voice-enabled AI assistant that understands English, Tamil, and Hindi, answers questions, opens websites, tells time, and provides spoken responses using text-to-speech. Perfect for multitasking or hands-free interaction.

✨ Key Features

Multi-language Voice Recognition – Understands English (EN), Tamil (TA), and Hindi (HI).

AI-Powered Answers – Quick, concise responses via Google Gemini API.

Voice-Activated Web Navigation – Open YouTube, Google, Instagram, and more.

Time & Simple Conversations – Ask the assistant for the current time or casual talk.

Text-to-Speech – Every response is displayed and spoken aloud.

Safe API Management – API keys stored securely in .env (not pushed to Git).

🎤 Usage

Speak commands like:

"Open YouTube"

"What’s the time?"

Ask general questions for AI-powered answers (both displayed and spoken).

To exit the assistant:

Say "Exit" or "Quit"

Folder Structure
Multilingual-AI-Assistant/
│

├─ VoiceAssistant.py       # Main assistant code

├─ requirements.txt        # Python dependencies

├─ .env                    # API key (not tracked in Git)

├─ README.md               # Project documentation

└─ ...                     # Additional resources

🛠 Dependencies

Python 3.x

pyttsx3 – Text-to-Speech

speech_recognition – Voice input

python-dotenv – Load API keys from .env

google-generativeai – Gemini API client

webbrowser – Open websites

⚠️ Important Notes

Do not commit .env – it contains sensitive API keys.

Ensure your system microphone access is enabled.

Gemini API usage may be limited by daily quota.

💡 Enhancements & Future Work

Add more languages and custom commands.

Integrate with calendar, email, or messaging apps.

Support offline voice commands for privacy.
