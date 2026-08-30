import google.generativeai as genai
import speech_recognition as sr
import win32com.client

speaker = win32com.client.Dispatch("SAPI.spvoice")

def speak(text):
    speaker.speak(text)
    print("jarvis:", text)
    speaker.speak(text)

genai.configure(api_key="YOUR_GEMINI_KEY")
model = genai.GenerativeModel("gemini-pro")

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
  response = model.generative_content(question)
  return response.text
  model="gpt-3.5-turbo"
  
  return response.choices[0].message.content


speak("hello boss , i am jarvis powered by GEMINI AI!")


while True:
    query = listen()

    if query is None:
        continue
    
    if "stop" in query.lower() or "exit" in query.lower():
        speak("goodbye!")
    break

answer = ask_jarvis(query)
speak(answer)
