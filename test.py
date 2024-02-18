'''import requests
#import folium
res=requests.get('https://ipinfo.io/')
data = res.json()
print(data)


def secondCmd():
    if sr.Microphone is True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)

        try:
            print("Recognizing...")
            cmd = r.recognize_google(audio)
            print(f" you said : {cmd}\n")

        except Exception as e:
            print(e)
            print("Say that again please...")
            return "None"

    else:
        print("mic is not connect")
        cmd = input()

    return cmd


import time
import pyautogui

def close_all_software():
    # Wait for a short delay before starting
    time.sleep(2)

    # Simulate pressing the Alt+F4 keyboard shortcut multiple times
    for _ in range(10):
        pyautogui.hotkey('alt', 'f4')
        time.sleep(0.5)

close_all_software()
from close_the_app import close_app
from getallapps import  list_of_software

for i in list_of_software():
    close_app(i)
import os
import subprocess

# Get the running processes
process = subprocess.Popen(['tasklist'], stdout=subprocess.PIPE)
output, _ = process.communicate()

# Parse the output to get process names
process_names = [line.split()[0].decode() for line in output.splitlines()[3:]]

# Terminate each process
for name in process_names:
    os.system(f"taskkill /F /IM {name}")




import os
os.startfile("C:\\Users\\fortever\\Downloads")

def tester():
    enter = input("fdfd: ")
    list_a = []
    i =0
    while i < 5:
        if enter == "1" :
            cmd = input()
            list_a.append(cmd)
        elif enter == 2:
            cmd = input("dfd")
            list_a.append(cmd)
        i = i+1

    return list_a

simple = tester()

import time
import pygetwindow as gw
import pyautogui

# Wait for Chrome window to be active
chrome_window = None
while not chrome_window:
    chrome_window = gw.getWindowsWithTitle('Google Chrome')[0]
    time.sleep(1)

# Bring Chrome window to the front
chrome_window.activate()

# Switch to the Instagram tab
pyautogui.hotkey('Ctrl', 'Tab')
time.sleep(0.5)  # Wait for the tab switch to complete

# Close the active tab
pyautogui.hotkey('Ctrl', 'w')

import pyaudio

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Get the number of available audio devices
num_devices = audio.get_device_count()

# Check if any microphone device is found
is_microphone_connected = False
for i in range(num_devices):
    device_info = audio.get_device_info_by_index(i)
    if device_info["maxInputChannels"] > 0:
        is_microphone_connected = True
        break

# Print the microphone connection status
if is_microphone_connected:
    print("Microphone is connected.")
else:
    print("Microphone is not connected.")

# Terminate PyAudio
audio.terminate()



pywhatkit.sendwhatmsg("+919025328897",
					"Geeks For Geeks!",
					22, 59
                      )

import speech_recognition as sr

# Create a recognizer object
recognizer = sr.Recognizer()

# Use the default microphone as the audio source
with sr.Microphone() as source:
    print("Speak something...")
    audio = recognizer.listen(source)

    try:
        # Recognize speech using Google Speech Recognition with English (India) language
        text = recognizer.recognize_google(audio, language="en-IN")
        print("You said: " + text)
    except sr.UnknownValueError:
        print("Sorry, I could not understand your speech.")
    except sr.RequestError as e:
        print("Error occurred: {0}".format(e))

import pywhatkit


pywhatkit.sendwhatmsg_instantly(
    phone_no="+91 90253 28897",
    message="Howdy! This message will be sent instantly!",
)

from collections import deque

# Declaring deque
while True:
    queue = deque(['name', 'age', 'DOB'])

    print(queue)
    enter = input()

    queue.append(enter)
    print(queue)
'''
