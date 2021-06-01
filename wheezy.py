import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import json
import requests
import newsapi

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)

engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    # pass


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour == 0 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Evening Sir!")
    else:
        speak("Good Evening Sir!")
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
        return "None"
    return query


def work():
    while True:
        query = takeInput().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According To Wikipedia")
            print(results)

            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open netflix' in query:
            webbrowser.open("netflix.com")
        # elif 'play music' in query:
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
        elif 'open whatsapp' in  query:


if __name__ == '__main__':

    while True:
        # job = takeInput().lower()
        # if 'there' in job:
            wishme()
            work()

    # takeInput()
