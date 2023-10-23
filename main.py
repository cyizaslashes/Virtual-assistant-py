import speech_recognition as sr
import pyttsx3

listener = sr.Recognition()
engine = pyttsx3.init()
voices= engine.getProperty('voices')
engine.setproperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

try:
    with sr.microphone() as source:
        print('listening....')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if 'alexa' in command:
            talk(command)
except:
    pass
