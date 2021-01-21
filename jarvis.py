import pyttsx3
import datetime
import speech_recognition as sr
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning")
    elif hour>=12:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("How may i help you!")
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone as source:
        print("Listening...")
        sr.pause_threshold = 1
        audio = sr.listen(source)
    try:
        print("Recognising...")
        query = sr.recognize_google(audio, language = 'en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please....")
        return 'none'
if __name__ == "__main__":
    # wishMe()
    takeCommand()