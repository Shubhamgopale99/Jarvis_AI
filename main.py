import speech_recognition as sr
import os
import webbrowser
import openai
def say(text):
    os.system(f"say {text}")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.5
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some error occurred. sorry from jarvis"


if __name__ == '__main__':
    print('PyCharm')
    say("Hello I am Jarvis A.I")
    while True:
        print("Listening...")
        query = takeCommand()
        sites = [["Youtube", "https://www.youtube.com"], ["Wikipidia", "https://www.wikipedia.com"], ["Google", "https://www.google.com"]]
        for site in sites:
            if f"open {site[0]}" .lower() in query.lower():
                say(f"Opening {site[0]} sir...")
                webbrowser.open(site[1])

            if "open music" in query:
                musicPath = r'C:\Users\User\Downloads\Kgf Bgm-sound.mp3'
                os.startfile(musicPath)

            if "Open Barish".lower() in query .lower():
                say("Opening Baarish Song sir...")
                webbrowser.open("https://youtu.be/EFqkHIMbhQg")

            if "Open Google".lower() in query .lower():
                say("Opening Google sir...")
                webbrowser.open("https://google.com")

        #say(query)