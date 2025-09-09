import speech_recognition as sr
import webbrowser
import pyttsx3
import musicliberary  
from openai import OpenAI
import os


# Initialize text-to-speech engine
engine = pyttsx3.init()


def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()


def aiprocess(command: str) -> str:
    """Send command to OpenAI API and return response."""

    
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return "Error: OpenAI API key not set. Please set OPENAI_API_KEY environment variable."

    client = OpenAI(api_key=api_key)

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa or Google Assistant."},
            {"role": "user", "content": command},
        ]
    )

    return completion.choices[0].message.content


def processCommand(c: str):
    """Process user voice commands."""
    if "open google" in c.lower():
        webbrowser.open('https://google.com')
    elif "open facebook" in c.lower():
        webbrowser.open('https://facebook.com')
    elif "open youtube" in c.lower():
        webbrowser.open('https://youtube.com')
    elif "open linkedin" in c.lower():
        webbrowser.open('https://linkedin.com')
    elif c.lower().startswith('play'):
        song = c.lower().split(" ", 1)[1]  
        if song in musicliberary.music:
            link = musicliberary.music[song]
            webbrowser.open(link)
        else:
            speak(f"Sorry, I couldn’t find {song} in your music library.")
    else:
        output = aiprocess(c)
        speak(output)


if __name__ == "__main__":
    speak("Initializing Jarvis...")
    while True:
        r = sr.Recognizer()
        print("Recognising...")

        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=2)
            word = r.recognize_google(audio)

            if word.lower() == 'jarvis':
                speak('Yes?')
                with sr.Microphone() as source:
                    print('Jarvis active...')
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)

        except Exception as e:
            print(f"Error: {e}")
