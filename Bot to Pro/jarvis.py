import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser

# Initialize text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    """Speak out the given text."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to microphone and return text."""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}")
    except Exception:
        speak("Sorry, I didn't catch that. Please say again.")
        return ""
    return query.lower()

def wish_me():
    """Greet the user based on time."""
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        speak("Good morning! Iam Jarvis how can help you Dhanish Rai, what are you doing. Do you enjoy my company")

    elif hour < 18:
        speak("Good afternoon!")
        
    else:
        speak("Good evening!")
    speak("I am Jarvis. How can I help you?")

if __name__ == "__main__":
    wish_me()
    while True:
        command = listen()

        if "time" in command:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {time}")

        elif "open google" in command:
            webbrowser.open("https://google.com")
            speak("Opening Google")

        elif "stop" in command or "quit" in command:
            speak("Goodbye!")
            break