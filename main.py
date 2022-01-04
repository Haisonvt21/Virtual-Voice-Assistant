 
import speech_recognition as sr
import datetime
import pyttsx3 as pytt
import wikipedia
import pywhatkit
import datetime
import sys
     
engine = pytt.init('sapi5')# Microsoft Speech API engine
voices = engine.getProperty ('voices')
engine.setProperty ('voice',voices [1].id) # 0 --> male voice 1--> Female voice
def wishMe () :
    hour = int (datetime.datetime.now() .hour)
    if hour>=0 and hour<12:
         speak ('Good Morning')
    elif hour>=12 and hour<18:
         speak ('Good Afternoon')
    else:
         speak ('Good Evening')
def speak (text):
    engine.say (text)
    engine.runAndWait()
wishMe()
speak ('Hello Sir , I am Siri, how can i help you')
# obtain audio from the microphone
r = sr.Recognizer()
def take_command():
    try:
        with sr.Microphone() as source:
            print("Say something!")
            voice = r.listen(source)
            # Recognizes speech using Google as a service: online
            text = r.recognize_google(voice,language="en-US")
            text=text.lower()
            if 'siri' in text:
                text =text.replace('siri', '')
                print(text)
    except:
        pass
    return text
def run_siri():
    text2 = take_command()
    text2=text2.lower()
    print(text2)
    if 'are you there' in text2:
        speak("I'm here sir")
    elif 'play' in text2:
        song = text2.replace('play', '')
        speak('playing '+song)
        pywhatkit.playonyt(song)
    elif 'time' in text2:
        time = datetime.datetime.now().strftime('%I:%M %p')
        speak('Current time is ' + time)
        print(time)
    elif 'today' in text2:
        date = datetime.datetime.now().strftime('%A-%d')
        speak('Current date is ' + date)
        print(date)
    elif 'who is' in text2:
        person = text2.replace('who is', '')
        info = wikipedia.summary(person,sentences=1)
        print(info)
        speak(info)
    elif 'what is' in text2:
        thing = text2.replace('what is', '')
        info = wikipedia.summary(thing,sentences=2)
        print(info)
        speak(info)
    elif 'stop' in text2:
        print('Have a goood day')
        sys.exit()
    else:
        print('you said: ',text2)
        return run_siri()
while True:
    run_siri()
