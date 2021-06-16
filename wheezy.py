import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import json
import requests
import sys
import pyjokes
import wolframalpha
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    global user
    speak("Hey what can I call you?")
    user = takeInput().lower()
    if hour == 0 and hour < 12:
        speak(f"Good Morning{user}")

    elif hour >= 12 and hour < 18:
        speak(f"Good Evening{user} ")
    else:
        speak(f"Good Evening{user}")
    speak("I am Wheezy. How may I help You?")


def takeInput():
    '''Take User input through microphone & returns string output'''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"User Said:{query}\n")
    except Exception as e:
        print("Say That Again Please...")

        return 'None'
    return query


def maps():
        query= takeInput().lower()
        query = query.split(" ")
        speak(f"Hold on {user}, I will show you where " + query[2] + " is.")
        location_url = "https://www.google.com/maps/place/" + str(query[2])
        webbrowser.open(f"{location_url}")


def assignment():
    while True:
        global query
        query = takeInput().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According To Wikipedia")
            print(results)
            speak(results)

        elif 'how are you' in query:
            list = ['good', 'fine', 'great']
            response = random.choice(list)
            speak(f"I am{response}")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open netflix' in query:
            webbrowser.open("netflix.com")

        elif 'news' in query:
            url = ('https://newsapi.org/v2/top-headlines?country=in&apiKey=c6262b55a16b409a84240667653e633b')
            response = requests.get(url)
            text = response.text
            data = json.loads(response.content)
            speak("Latest News Headlines are : ")
            for i in range(0, 11):
                collect = data['articles'][i]['title']
                speak(i + 1)
                speak(collect)
                print("News", i + 1, ":", collect)

        elif 'jokes' in query:
            joke = pyjokes.get_joke()
            print(joke)
            speak(joke)

        elif 'where is' in query:
            maps()

        elif 'what' in query or 'solve' in query:
            app_id = ['QU44UH-WRV2R7URUP']
            client = wolframalpha.Client(app_id)
            res = client.query(query)
            answer = next(res.results).text
            print(answer)
            speak(answer)

        elif 'quit' in query or 'exit' in query:
            exit()

if __name__ == '__main__':
    while True:
        say = takeInput().lower()
        wishme()
        assignment()
        if 'exit' in say:
            sys.exit()
