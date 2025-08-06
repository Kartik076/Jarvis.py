# 🧠 Jarvis - Voice Assistant in Python

Jarvis is a simple Python-based desktop voice assistant that can perform tasks like opening websites, fetching weather data, playing music, launching apps, and more using voice commands.

## 📅 Last Updated

**13/07/2024**

## 📌 Features

- ✅ Voice-activated assistant with wake word **"Jarvis"**  
- 🔍 Search YouTube  
- 📺 Open common websites (Google, YouTube, ChatGPT, Chrome, etc.)  
- 🎵 Play songs from a predefined library or search YouTube  
- 🌦️ Get current weather updates (using OpenWeather API)  
- 💻 Launch local apps (e.g., Brave, Lenovo Vantage)  
- 💡 Adjust brightness  
- 🔁 Repeat what you say (until you say "done")  

## 🛠️ Tech Stack

- Python 3.x  
- [pyttsx3](https://pypi.org/project/pyttsx3/) – Text-to-speech engine  
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) – Speech recognition  
- [PyAudio](https://pypi.org/project/PyAudio/) – Microphone input  
- [webbrowser](https://docs.python.org/3/library/webbrowser.html) – Open URLs  
- [requests](https://docs.python.org/3/library/requests.html) – API requests  
- [pyautogui](https://pypi.org/project/PyAutoGUI/) – UI automation  
- Custom `musiclibrary.py` – Dictionary of song names mapped to YouTube URLs  

## ⚙️ Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/Jarvis.git
   cd Jarvis
Install dependencies:

bash
Copy
Edit
pip install pyttsx3 SpeechRecognition PyAudio requests pyautogui
Configure microphone and permissions:
Ensure your microphone works and is accessible by Python.

Add your OpenWeather API key (optional):
Replace the api_key in the script with your own key for weather functionality.

Run Jarvis:

bash
Copy
Edit
python jarvis.py
🗣️ How to Use
Say "Jarvis" to wake the assistant.

Use commands like:

"Open YouTube"

"Search [your query]"

"Play [song name]"

"Weather"

"Increase brightness"

"Repeat" (to repeat what you say until you say "done")

🎵 musiclibrary.py Example
Create a file named musiclibrary.py with:

python
Copy
Edit
music = {
    "shape of you": "https://www.youtube.com/watch?v=JGwWNGJdvx8",
    "blinding lights": "https://www.youtube.com/watch?v=4NRXx6U8ABQ",
    # Add more songs here
}
🛡️ Git Safety Note
If you encounter dubious ownership errors with Git, run:

bash
Copy
Edit
git config --global --add safe.directory "D:/VScode/Python/Jarvis"
⚠️ Troubleshooting
Check microphone permissions if speech recognition fails.

Modify city name in the weather function to your location.

Adjust pyautogui coordinates based on your screen resolution.
