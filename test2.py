from vosk import Model, KaldiRecognizer
import os
import pyaudio
import pyttsx3
import json
import datetime
import subprocess
import webbrowser
import sys


# Import the core lib
from core import SystemInfo
from core.system import Runner

# Import NLU classifier
from nlu.classifier import classify

# Runner
runner = Runner()

# Speech Synthesis
engine = pyttsx3.init('sapi5')# Microsoft Speech API engine
voices = engine.getProperty ('voices')
engine.setProperty ('voice',voices [1].id) # 0 --> male voice 1--> Female voice
def wishMe():
    hour = int (datetime.datetime.now() .hour)
    if hour>=0 and hour<12:
         speak ('Good Morning')
    elif hour>=12 and hour<18:
         speak ('Good Afternoon')
    else:
         speak ('Good Evening')
# Function
def speak (text):
    engine.say (text)
    engine.runAndWait()
wishMe()
speak ('I am Siri, how can i help you')
url = 'https://www.google.com/'
def evaluale(text):
    entity = classify(text)        
    if entity == 'time\\getTime':
        print(datetime.datetime.now().strftime('%I-%M %p'))
        speak(SystemInfo.get_time())
    if entity == 'time\\getDate':
        print(datetime.datetime.now().strftime('%A-%d'))
        speak(SystemInfo.get_date())
    elif entity == 'time\\getYear':
        print(datetime.datetime.now().strftime('%G'))
        speak(SystemInfo.get_year())
    elif entity == 'open\\chrome':
        speak('opening chrome') 
        webbrowser.open(url)
    elif str(text).lower()=='stop':
        sys.exit()
    else:
            pass
# Speech Recognition

model = Model("model")
rec = KaldiRecognizer(model, 16000)

# Opens microphone for listening.
p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=4096)
stream.start_stream()
print("Say something!")
while True:
    data = stream.read(4000)
    if len(data) == 0:
        break
    if rec.AcceptWaveform(data):
        result = rec.Result()
        #result is a string, convert to a json/dictionary
        result= json.loads(result)
        text = result['text']
        print('you said: ',text)
        evaluale(text)
        
       

    



        

