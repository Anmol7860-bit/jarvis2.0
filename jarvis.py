import speech_recognition as sr
import webbrowser
import pyttsx3
import musicliberary
from openai import Openai
recogniser=sr.recognizer
engine=pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def aiprocess(command):
    client = OpenAI(
    api_key='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',)
    completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like alexa and google cloud."},
        {
            "role": "user",
            "content": command
        }
    ]
    )
    return completion.choices[0].message.content
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open('https://google.com')
    elif "open facebook" in c.lower():
        webbrowser.open('https://facebook.com')
    elif "open youtube" in c.lower():
        webbrowser.open('https://youtube.com')
    elif "open linkedin" in c.lower():
        webbrowser.open('https://linkedin.com')
    elif c.lower().startswith('play'):
        song=c.lower().split(" ")[1]
        link=musicliberary.music[song]
        webbrowser.open(link)
    else:
        output=aiprocess
        speak(output)

    

    
if __name__ =="__main__":
    speak("initializing Jarvis......")
    while True:
    # obtain audio from the microphone
        r = sr.Recognizer()
        # recognize speech using Sphinx
        print("recognising...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
            word=r.recognize_google(audio)
            if (word.lower()=='jarvis'):
                speak('ya')
                with sr.Microphone() as source:
                    print('jarvis active')
                    audio=r.listen(source)
                    command=r.recognize_google(audio)

                    processCommand(command)
        except Exception as e:
            print("error; {0}".format(e))