import numpy as np
import speech_recognition as sr
import win32com.client
from sklearn.linear_model import LinearRegression

speaker = win32com.client.Dispatch("SAPI.spvoice")

def speak(text):
    speaker.speak(text)


    x = np.array([1, 2, 3, 4, 5, 6 ]).reshape(-1,1)
    y = np.array([40, 50, 60, 70, 80, 90])

    model = LinearRegression()
    model.fit(x, y)


def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
         speak("Tell me study hours")
         audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        return float(command)
    except:
         speak("sorry, I didn't understand")
         return None
    
speak("HELLO BOSS, I AM JARVIS MINI, YOUR PERSONAL ASSISTANT")
hours = listen()


if hours is not None:
    prediction = model.predict([[hours]])
    speak(f"you may score approximately {int(prediction[0])} marks")
    print("prediction Marks:", prediction[0])
