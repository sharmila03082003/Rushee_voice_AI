import sys
import time as ti
import pywhatkit
import speech_recognition as sr
import pyttsx3
import webbrowser
import datetime
import os as os
import subprocess as sp
import pyjokes
import wikipedia
import ctypes
import random
from getallapps import get_to_open
from close_the_app import close_app




engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
list_of_apps_opend = []
r = sr.Recognizer()



def firsttalk(talk):
    engine.say(talk)
    engine.runAndWait()


def secondCmd():


    if sr.Microphone is True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source, timeout=1, phrase_time_limit=5)

        try:
            print("Recognizing...")
            cmd = r.recognize_google(audio, language='en-in')
            print(f"You said: {cmd}\n")


        except Exception as e:
            print("Speech recognition could not understand audio")
            return "none"

        return cmd
    else:
        print("Microphone is not connected")
        cmd = input("Enter cmdand: ")
        return cmd



def wish():
    hour = datetime.datetime.now().hour

    if hour >= 0 and hour < 12:
        print("Good Morning!")
    elif hour >= 12 and hour < 18:
        print("Good Afternoon!")
    elif hour >= 18 and hour < 20:
        print("Good Evening!")
    elif hour >= 20 and hour < 24:
        print("Good Night!")
    else:
        print("Good Night!")



def starting():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        gm = [
            "Good Morning!!!  A new blessing and a new day is waiting for you.",
            "A very Good Morning!!! I hope your morning is as bright as your smile.",
            "It always seems impossible until it’s done. Move ahead and finish it. Good Morning.",
            "Good Morning!!! You have to get up every morning and tell yourself that I can do it.",
            "Think positive, stay happy and test negative.” Go Corona… Good Morning!!!Good Morning",
            "Wake up every morning with the thought that something wonderful is about to happen.",
            "I love the smell of possibility in the morning. Good Morning!", ]
        gmm = random.choice(gm)
        firsttalk(gmm)

    elif hour >= 12 and hour < 18:
        firsttalk("how the day was going , i hope it will be nace day to you sir")
    elif hour >= 20 and hour < 23:
        gn = [
            "For thousands of nights, I dreamed of making love to you. No man on Earth has ever hated sunrise as I do.",
            "Star Light, star bright, you are the first and last I think of tonight. Good night, my true love.",
            "No matter how far away you are, you will always be in my thoughts. Each day that we are together is the best day of my life.",
            "You are the best thing that’s ever been mine.",
            "Once upon a time there was a boy who loved a girl and her laughter was a question he wanted to spend his whole life answering.",
            "We are made of particles that existed since the moment the universe began. I like to think those atoms traveled 14 billion years through time and space to create us so that we could be together and make each other whole.",
            "I love that you are the last person I want to talk to before I go to sleep at night.",
            "I have found the one whom my soul loves.",
            "And tonight, I’ll fall asleep with you in my heart.",
            "You are my blue crayon—the one I never have enough of—the one I use to color my sky.",
            "I’d choose you, in a hundred lifetimes, in a hundred worlds, in any version of reality, I’d find you and I’d choose you.",
            "I don’t wanna close my eyes, I don’t wanna fall asleep, cuz I’d miss you babe and I don’t wanna miss a thing.",
            "The day is busy enough to keep me occupied. In the quiet of the night, I begin to really miss you.",
            "Good night, good night! Parting is such sweet sorrow, that I shall say good night till it be morrow."
        ]
        gnn = random.choice(gn)
        print(gnn)
        firsttalk(gnn)
    else:
        firsttalk("")

def thecmdrushe():
    while True:
        cmd = secondCmd()
        cmd = cmd.lower()

        if "wake up" in cmd or "rush" in cmd or "ok rush" in cmd or "ok rushe" in cmd:
            firsttalk("i am ready sir , please tell me what can i do for you. ")
            while True:
                cmd_two = secondCmd()
                cmd_two = cmd_two.lower()
                op = "opening"
                if "play" in cmd_two.lower():
                    music = cmd_two.replace('play', '')
                    print(music)
                    firsttalk("playing")
                    pywhatkit.playonyt(music)

                elif "some joke" in cmd_two.lower():
                    jk = pyjokes.get_joke()
                    print(jk)
                    firsttalk(jk)


                elif "who is " in cmd_two or "what is" in cmd_two:
                    person = cmd_two.replace('who is ', '')
                    info = wikipedia.summary(person, 1)
                    print(info)
                    firsttalk(info)
                elif "open download" in cmd_two or "open download path" in cmd_two:
                    os.startfile("C:\\Users\\fortever\\Downloads")     #replace your user path
                elif "open video" in cmd_two or "open video path"  in cmd_two:
                    os.startfile("C:\\Users\\fortever\\Video")     #replace your user path
                # close app
                elif "close " in cmd_two.lower():
                    firsttalk("ok")
                    place = cmd_two.replace('close','')
                    place = place.lstrip()
                    print(place)
                    close_app(place)
                # open apps
                elif "open " in cmd_two.lower():
                    firsttalk(op)
                    place = cmd_two.replace('open','')
                    place = place.lstrip()
                    print(place)
                    get_to_open(place)

                elif "time now" in cmd_two.lower():
                    time = datetime.datetime.now().strftime('%I %M %p')
                    print(time)
                    firsttalk("The current time is" + time)
                elif "where is" in cmd_two:
                    location = cmd_two.replace("where is", "")
                    firsttalk("searching" + location)
                    webbrowser.open("https://www.google.com/maps/place/" + location)
                elif "go to study" in cmd_two.lower() or "study mode" in cmd_two.lower():
                    # firsttalk("which one you want sir")
                    webbrowser.open("https://swayam.gov.in/")

                elif "music" in cmd_two or "play some music " in cmd_two.lower():
                    song = os.listdir("E:\\Music\\Songs")
                    os.startfile(os.path.join("E:\\Music\\Songs", song[5])) #replace your user path
                    break
                elif "see you later" in cmd_two.lower():
                    print("see you later , sir ")
                    exit()
                elif "go to sleep" in cmd_two:
                    firsttalk("OK ")
                    print("if you say 'rush' only , I will come back")
                    break
                elif "power off " in cmd_two.lower() or "poweroff" in cmd_two.lower():
                    firsttalk("Your system will be power off in few seconds")
                    os.system("shutdown /s /t 5")
                    os.system('taskkill /F /IM *')
                    sys.exit()
                elif "restart my pc" in cmd_two.lower() or "restart my computer" in cmd_two.lower():
                    firsttalk("your system will be Restart in few seconds ")
                    os.system("shutdown /r /t  1")
                    ti.sleep(1)
                    sys.exit()
                elif "lock my pc" in cmd_two.lower() or "lock my computer" in cmd_two.lower():
                    firsttalk("ok")
                    ctypes.windll.user32.LockWorkStation()
                elif "notepad" in cmd_two.lower() or "Notepad " in cmd_two:
                    notepad = "notepad.exe"
                    filename = "file.txt"
                    sp.Popen([notepad, filename])
                elif "movie folder" in cmd_two.lower():
                    mf = "which movie folder , I want to open sirrr " + "Normal movie fooo" \
                                                                        "lder or telegram path"
                    print(mf)
                    firsttalk(mf)
                    mfs = secondCmd().lower()
                    if "one" in mfs.lower() or "normal movie" in mfs.lower() or "1" in mfs.lower():
                        firsttalk("opening")
                        os.startfile("D:\\Movie") #replace your user path
                    elif "two" in mfs.lower() or "telegram" in mfs.lower() or "2" in mfs.lower():
                        firsttalk("opening")
                        os.startfile("E:\\cDownloads\\Telegram Desktop") #replace your user path
                    else:
                        print("can't hear you , sir")
                # elif "send email" in cmd_two.lower() or "send a email" in cmd_two.lower():
                # smail()

                elif "what is temperature" in cmd_two.lower():
                    pass
                # shut down
                elif "power off" in cmd_two.lower():
                    firsttalk("Your system will be power off in few seconds ")
                    os.system("shutdown /s /t 1")
                    exit()
             

if __name__ == "__main__":
    wish()
    starting()
    firsttalk("welcome sir , I am rushe your assistant ")
    thecmdrushe()
