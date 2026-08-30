import datetime
import os
import platform
import google.generativeai as genai
import psutil
import pyautogui
import pyttsx3
import pywhatkit
import speech_recognition as sr
import webbrowser
import wikipedia
 
# ========== AI (Gemini) ==========
API_KEY = os.environ.get("GEMINI_API_KEY")
if not API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY is not set. Set it as an environment variable before running "
        "(see the setup notes at the top of this file)."
    )
 
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")
 
 
def ask_ai(prompt: str) -> str:
    """Fallback: send anything Jarvis doesn't recognize to Gemini."""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as exc:  # noqa: BLE001
        return f"I couldn't reach the AI model: {exc}"
 
 
# ========== VOICE ENGINE ==========
engine = pyttsx3.init()
engine.setProperty("rate", 180)
 
 
def speak(text: str) -> None:
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()
 
 
# ========== LISTEN ==========
def take_command() -> str:
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
 
    try:
        command = r.recognize_google(audio)
        print("You:", command)
        return command.lower()
    except sr.UnknownValueError:
        return "nothing"
    except sr.RequestError as exc:
        speak("Speech recognition service is unavailable right now.")
        print("RequestError:", exc)
        return "nothing"
 
 
# ========== SYSTEM STATUS ==========
def system_status() -> None:
    cpu = psutil.cpu_percent(interval=1)
    battery = psutil.sensors_battery()
    speak(f"CPU usage is {cpu} percent")
    if battery:
        speak(f"Battery is at {battery.percent} percent")
    else:
        speak("No battery information available on this device.")
 
 
# ========== SHUTDOWN (cross-platform) ==========
def shutdown_system() -> None:
    speak("Shutting down system")
    system_name = platform.system()
    if system_name == "Windows":
        os.system("shutdown /s /t 5")
    elif system_name == "Darwin":  # macOS
        os.system("sudo shutdown -h +0")
    elif system_name == "Linux":
        os.system("shutdown -h now")
    else:
        speak(f"I don't know how to shut down a {system_name} system.")
 
 
# ========== MAIN COMMAND ENGINE ==========
def run_jarvis() -> None:
    speak("Jarvis activated. How can I help you?")
 
    while True:
        command = take_command()
 
        if command == "nothing":
            continue
 
        if "time" in command:
            current_time = datetime.datetime.now().strftime("%H:%M")
            speak(f"The time is {current_time}")
 
        elif "who is" in command:
            person = command.replace("who is", "").strip()
            try:
                info = wikipedia.summary(person, sentences=2)
                speak(info)
            except wikipedia.exceptions.DisambiguationError as exc:
                speak(f"That's ambiguous. Did you mean one of: {', '.join(exc.options[:5])}?")
            except wikipedia.exceptions.PageError:
                speak(f"I couldn't find a Wikipedia page for {person}.")
 
        elif "open youtube" in command:
            webbrowser.open("https://youtube.com")
            speak("Opening YouTube")
 
        elif "open google" in command:
            webbrowser.open("https://google.com")
            speak("Opening Google")
 
        elif "play" in command:
            song = command.replace("play", "").strip()
            speak(f"Playing {song} on YouTube")
            pywhatkit.playonyt(song)
 
        elif "search" in command:
            query = command.replace("search", "").strip()
            webbrowser.open(f"https://google.com/search?q={query}")
            speak(f"Searching for {query}")
 
        elif "system status" in command:
            system_status()
 
        elif "shutdown" in command:
            shutdown_system()
 
        elif "screenshot" in command:
            img = pyautogui.screenshot()
            img.save("screenshot.png")
            speak("Screenshot taken and saved as screenshot.png")
 
        elif "exit" in command or "stop" in command:
            speak("Goodbye")
            break
 
        else:
            # Fallback: anything unrecognized goes to Gemini instead of
            # being silently ignored.
            answer = ask_ai(command)
            speak(answer)
 
 
# ========== START ==========
if __name__ == "__main__":
    run_jarvis()
 