import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes
from sklearn.model_selection import PoissonRegressor
listener = sr.Recognizer()#sunar jonno listener namer object create kora holo
tom = pyttsx3.init()#tom namer object create kora holo
voice = tom.getProperty('voices')#
tom.setProperty('voice', voice[1].id)#female voice set kora holo
tom.say("Hello, How can I help you?")
tom.runAndWait()#tom er command run kora holo


def talk(text):
    tom.say(text)
    tom.runAndWait()
def talk_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "Tom" in command:
                    command = command.replace('Tom', '')
                    print(command)
                    
            #print(command)
            #return command

             

    except:
        return ""


            


def run_tom():
    command=talk_command()
    if  'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('current time is'+time)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing'+song)
        pywhatkit.playonyt(song)#youtube e song play korar jonno pywhatkit er playonyt function use kora holo
    elif 'tell me about' in command:
        look_for=command.replace('tell me about', '')
        info = wikipedia.summary(look_for, sentences=1)
        talk(info)
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        talk(joke)
    elif 'date' in command:
        talk('sorry, I have a boyfriend')
    else:
        talk('i do not understand but i will search for you.')
        pywhatkit.search(command)

while True:
    run_tom()

