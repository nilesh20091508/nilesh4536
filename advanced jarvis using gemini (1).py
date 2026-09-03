import win32com.client
import speech_recognition as sr
import google.generativeai as genai
import pyttsx3
import pyaudio

speaker = win32com.client.Dispatch("sapi voice")  
api_key =("AIzaSyCitX9wvUvoywPOKdNV4k1mGWtl7Xb1rtg")
genai.configure(api_key=api_key)

def speak(text):
    speaker.speak(text)
    print(":", text)
    speaker.speak(text)

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
         speak("Listening...")
         r.adjust_for_ambient_noise
         audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print("you said")
        return command
    except:
         speak("sorry, I didn't understand")
         return None
    
def ask_jarvis(question):
  response = genai.GenerativeModel("gemini-2.0-flash").generate_content(question)
  return response.text


speak("hello, i am jarvis powered by GEMINI AI!")

#listen for user input aand response the desired answer:
while True:
    query = listen()

    if query is None:
        continue
    
    if "stop" in query.lower() or "exit" in query.lower():
        speak("goodbye!")
        break

answer = ask_jarvis(query)
speak(answer)