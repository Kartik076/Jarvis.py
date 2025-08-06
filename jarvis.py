# Dated :- 13/07/2024
import pyttsx3
import speech_recognition as sr
import webbrowser
import pyaudio
import musiclibrary
import time
import pychromecast
import requests
import pyautogui


engine = pyttsx3.init()
recognizer = sr.Recognizer() 

# Set properties for clearer voice
engine.setProperty('rate', 180)  # Decrease the rate if the voice is too fast
engine.setProperty('volume', 1.0)  # Set volume level (0.0 to 1.0)

# Change voice to a clearer one if available
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # You can change the index to select different voices

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source , timeout=4 , phrase_time_limit=2)
    command = recognizer.recognize_google(audio)
    return command
    
def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        return weather
    else:
        print(f"Error fetching weather data: {response.status_code}")
        return None

def process(c):
    print(f'Command recognized :{c}')
    if "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
        speak("oppening youtube")

    elif "open google" in c.lower():
        webbrowser.open("https://www.google.com/")
        speak("oppening google")


    elif "open chat gpt" in c.lower():
        webbrowser.open("https://www.chatgpt.com/")
        speak("oppening chat g p T")


    elif "open chrome" in c.lower():
        webbrowser.open("https://www.chrome.com/")
        speak("oppening chrome")

    elif "open dsu" in c.lower():
        webbrowser.open("https://dseuadm.samarth.edu.in/index.php/site/")
        speak("oppening dseu website")

    elif "go to youtube history" in c.lower():
        webbrowser.open("https://www.youtube.com/feed/history")
        speak("going to youtube history")

    elif "go to youtube music" in c.lower():
        webbrowser.open("https://www.youtube.com/channel/UC-9-kyTW8ZkZNDHQJ6FgpwQ")
        speak("going to youtube music")

    elif "open lenovo" in c.lower():
        pyautogui.click(766, 1050)
        time.sleep(1)
        pyautogui.typewrite('lenovo vantage')
        pyautogui.press('enter')

    elif "open brave" in c.lower():
        pyautogui.click(766, 1050)
        time.sleep(1)
        pyautogui.typewrite('brave')
        pyautogui.press('enter')

    elif "increase brightness" in c.lower():
        pyautogui.press('brightnessup')
   
    elif c.lower().startswith("search"):
        word = "search "
        if word in c.lower():
            search = c[len(word):].strip()
            webbrowser.open(f"https://www.youtube.com/results?search_query={search}")
            speak(f"searching {search}")

    elif "weather" in c.lower():
        
        api_key = 'f7c31f91f84d91a3083e321e387f645e'
        city = 'Delhi'
        weather = get_weather(api_key, city)
        
        if weather:
            print(f"The weather in {weather['city']} is {weather['description']}.")
            speak(f"The weather in {weather['city']} is {weather['description']}.")
            print(f"The temperature is {weather['temperature']} degrees Celsius.")
            speak(f"The temperature is {weather['temperature']} degrees Celsius.")
            print(f"Humidity is {weather['humidity']} percent.")
            speak(f"Humidity is {weather['humidity']} percent.")
            print(f"Wind speed is {weather['wind_speed']} meters per second.")
            speak(f"Wind speed is {weather['wind_speed']} meters per second.")
        else:
            speak("Sorry, I couldn't fetch the weather data.")

    elif c.lower().startswith("play"):
        
        word = "play"
        if word in c.lower():
            song = c[len(word):].strip()

            try:
                if song in musiclibrary.music :
                    link = musiclibrary.music[song]
                    webbrowser.open(link)
                    speak(f"playing this song on youtube")

                elif True:
                    webbrowser.open(f"https://www.youtube.com/results?search_query={song}")
                    speak(f"openning this song on youtube")


            except Exception as e:
                print(e)

    elif c.lower().startswith("repeat"):

        print("ok sir")
        speak("ok sir")
        try:
            command = "ok"
            while command != "done":
                try:
                    command = listen()
                    speak(command)
                    print(command)
                    
                    if command == "done":
                        print("ok sir")
                        speak("ok sir")
                
                except Exception as e:
                    print(e)

        except Exception as e:
            print(e)

    
if __name__ == "__main__":
    
    speak("Initialising jarvis")
    
    while True:
        try:
            command = listen()

            if command.lower() == "jarvis":
                print(f"Command recognized: {command}")
                speak("yes sir")
                command = listen()
                process(command)

        except Exception as e:
            print(f'Error {e}')

