import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pyjokes
import pywhatkit

listner = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


engine.say('i am your alexa')
engine.say('what can i do for you')
engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening')
            voice = listner.listen(source)
            command = listner.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                talk(command)
    except:
        pass
    return command


def run_alexa():
    command = take_command()
    if 'play' in command:
        print(command)
        song = command.replace('play', '')
        talk('playing' + song)
        talk('playing')
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        talk('current time is' + time)
    elif 'who' in command:
        person = command.replace('who', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry i do not want to go')
    elif 'joke' in command:

        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())
    elif 'what' in command:
        person = command.replace('who', '')
        info = wikipedia.summary(person, 1)
        talk()
    else:
        talk('please say the command again')


while True:
    run_alexa()
