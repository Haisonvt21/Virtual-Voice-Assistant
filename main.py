import speech_recognition as sr
import datetime
import pyttsx3 as pytt
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
with sr.Microphone() as source:
    print("Say something!")
    while True:
        audio = r.listen(source)
        # Recognizes speech using Google as a service: online
        text = r.recognize_google(audio)
        if str(text).lower()== 'what time is it':
           print(datetime.datetime.now().strftime('%b-%d-%I%M%p-%G'))
           break
 