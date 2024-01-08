from tkinter import *
from PIL import Image
import speech_recognition as sr #pip install speechrecognition
from googletrans import Translator #pip install googletrans==3.1.0a0
import pyttsx3
import threading
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os


def MainExecution():
    print("")
    print("now me to introduce myself. i am SKIVVY . a virtual artificial intelegence and i am here to assist you with a variety of tasks. twentyfour hours a day seven days of week .  systems are now are fully operational.")
    print("")


    while True:

        Data = MicExecution()
        Data = str(Data)
        DataLen = len(Data)

        if "what is" in Data or "who " in Data or "question" in Data or "answer" in Data or "how" in Data or "tell me" in Data or "where" in Data:
            Reply = FriendChat(Data)
            Speak(Reply)

        if "introduce yourself" in Data:
           Speak("now me to introduce myself. i am SKIVVY . a virtual artificial intelegence and i am here to assist you with a variety of tasks. twentyfour hours a day seven days of week .  systems are now are fully operational.")
        elif int(DataLen)<=1:
            pass
        if 'wikipedia' in Data:
            Speak('Searching Wikipedia...')
            Data = Data.replace("wikipedia", "")
            results = wikipedia.summary(Data, sentences=2)
            Speak("According to Wikipedia")
            print(results)
            Speak(results)

        elif 'open youtube' in Data:
            webbrowser.open("youtube.com")

        elif 'open google' in Data:
            webbrowser.open("google.com")
        elif 'play music' in Data:
            music_dir = 'C:\\Users\\13nan\\Music\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in Data:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            Speak(f"Sir, the time is {strTime}")

        elif 'open code' in Data:
            codePath = "C:\\Users\\13nan\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codePath)

        elif 'hello' in Data:
            Speak(" hello sir i am skivy , i am there to help you out ")

        elif 'i am fine' in Data:
            Speak("happy to hear this nandini , hope you will recover from your anxiety soon")

        elif 'oh you care for me' in Data:
            Speak(" yes my lord, am there for you ")

        elif 'bye' in Data:
            Speak("bye sir hope to meet you soon ")

        elif 'thank you' in Data:
            Speak("most welcome sir")

        elif 'I am feeling alone and depressed' in Data:
            Speak("boss am there to help you out please do not feel lonely,share with me and light up your vibes")   

        else:
        	  url=Data
        	  r= requests.get("http://api.brainshop.ai/get?bid=171149&key=vUQ8EIQHjwgyJHYI&uid=[uid]&msg="+Data)
        	  if r.status_code == 200:
                     response_json = r.json()
                     d = response_json["cnt"]  
                     print(d)
                     Speak(d)
              else:
                 print("API request failed with status code:", r.status_code)
                 

root=Tk()
root.title("Skivvy")
root.configure(background="black")

#Functions
#Speak  
def Speak(Text):
    engine = pyttsx3.init("sapi5")
    voices = engine.getProperty('voices')
    engine.setProperty('voices',voices[1].id)
    engine.setProperty('rate',170)
    print("")
    print(f"You : {Text}.")
    print("")
    engine.say(Text)
    engine.runAndWait()

# 1. listen 
def Listen():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold=4000
        r.pause_threshold = 1
        audio = r.listen(source,0,None) # Listening Mode.....

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language="hi")

    except:
        return ""

    query = str(query).lower()
    return query

# 2 - Translation

def TranslationHinToEng(Text):
    line = str(Text)
    translate = Translator()
    result = translate.translate(line)
    data = result.text
    print(f"You : {data}.")
    return data

# 3 - Connect

def MicExecution():
    query = Listen()
    data = TranslationHinToEng(query)
    return data





file="/storage/emulated/0/python /fxVE.gif"




info = Image.open(file)
frames = info.n_frames
print(frames)
def animation(count):
    im2 = im[count]
    gif_label.configure(image=im2)

    count += 1
    if count == frames:
        count = 0

    root.after(50,lambda :animation(count))

im = [PhotoImage(file=file,format=f'gif -index {i}') for i in range(frames)]
gif_label = Label(root, image="")
gif_label.configure(background='black')
gif_label.pack()
count=0
text_view=Label(background="black",fg="white",text="",font=("Helvetica",15),)
text_view.pack()
b1=Button(root,text="Wake Up Me",fg="white",background="black",font=("Helvetica",15),command=animation(0))
b1.pack()


#WakeupDetected()

root.mainloop()