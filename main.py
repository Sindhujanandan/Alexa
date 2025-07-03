import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pyjokes
import pywhatkit

# Initialize recognizer and text-to-speech engine
listener = sr.Recognizer()
engine = pyttsx3.init()

# Set voice (optional: female voice if available)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id if len(voices) > 1 else voices[0].id)

# Speak function
def talk(text):
    try:
        engine.say(text)
        engine.runAndWait()
    except RuntimeError:
        pass  # Safeguard against "run loop already started"

# Listen and convert speech to text
def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            print("Listening...")
            listener.adjust_for_ambient_noise(source)
            audio = listener.listen(source, timeout=5)
            command = listener.recognize_google(audio)
            command = command.lower()
            print("You said:", command)
            if 'alexa' in command:
                command = command.replace('alexa', '').strip()
    except sr.WaitTimeoutError:
        print("Listening timed out.")
    except sr.UnknownValueError:
        print("Sorry, I did not understand that.")
    except sr.RequestError:
        print("Network error.")
    return command

# Main assistant function
def run_alexa():
    command = take_command()
    if command == "":
        talk("Sorry, I didn't catch that.")
        return

    try:
        if 'play' in command:
            song = command.replace('play', '').strip()
            talk('Playing ' + song)
            pywhatkit.playonyt(song)

        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)

        elif 'who is' in command or 'what is' in command:
            person = command.replace('who is', '').replace('what is', '').strip()
            try:
                info = wikipedia.summary(person, 1)
                print(info)
                talk(info)
            except wikipedia.exceptions.DisambiguationError:
                talk("There are multiple matches. Please be more specific.")
            except:
                talk("Sorry, I couldn't find information on that.")

        elif 'date' in command:
            talk("Sorry, I do not want to go on a date.")

        elif 'joke' in command:
            joke = pyjokes.get_joke()
            print(joke)
            talk(joke)

        elif 'exit' in command or 'stop' in command:
            talk("Goodbye!")
            exit()

        else:
            talk("Please say the command again.")
    except RuntimeError as e:
        print("Speech engine error:", e)

# Greet after everything is set up
talk("I am your Alexa. What can I do for you?")

# Main loop
while True:
    run_alexa()
