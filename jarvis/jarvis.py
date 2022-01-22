# search any in wikipedia using jarvis                  ==> EX. salmankhan according to wikipedia
# open youtube,google,instagam,facebook using jarvis    ==> Ex. jarvis open youtube
# play music using my music_dir in jarvis               ==> Ex. jarvis play music
# see time using jarvis                                 ==> Ex. jarvis what the time  
# see date using jarvis                                 ==> Ex. jarvis What the date
# open apps like vsCode , openOffice using jarvis       ==> Ex. jarvis open code/office  
from ast import Break
from re import search
from idlist import password, my_gmail, destination
import pyttsx3
import wikipedia
import speech_recognition as sr
import datetime
import webbrowser
import os
import smtplib
import pytz

p = password #this variable use to send e mail to destination
g = my_gmail
d = destination
print(p, g, d)

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0])
engine.setProperty('voices', voices[1].id )

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


 
def wishMe(): # this function is use to wish good evening and etc.
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    
    elif hour>=12 and hour<18:
        speak("Good AfterNoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis sir. Please tell me how may I help you?")

def takeCommand():
    #IT takes microphone input from the user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said:{query}\n")
 
     
    except Exception as e: # this function is use for when jarvis doesn't hear your voice
       # print(e)
        print("say that again....")
        return "None"
    return query
#send email through enable less secure app access and also use SMTP client as module
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo() # to connect our server to gmail
    server.starttls() # to provide security
    server.login(g, p)
    server.sendmail(g, to, content)
    server.close()
  
if __name__=="__main__":
     wishMe()
   #   while True:
     if 1:
        query = takeCommand().lower()
     # logic for the exicuting tasks based on query

     if 'wikipedia' in query: # this function is use to search in wikipedia using jarvis! 
        speak('Searching wikipedia....Please wait Result will show in some time')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)

     elif 'open youtube' in query: # this function is use to open websites in given below
        webbrowser.open("youtube.com")
     elif 'open instagram' in query:
        webbrowser.open("instagram.com") 
     elif 'open google' in query:
        webbrowser.open("google.com")
     elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")
     elif 'open w3schools' in query:
        webbrowser.open("w3schools.com")
     elif 'open programiz' in query:
        webbrowser.open("programiz.com")
     elif 'open geeksforgeeks' in query:
        webbrowser.open("geeksforgeeks.org")
     elif 'open facebook' in query:
        webbrowser.open("facebook.com")
      # write changes in music_dir path after unzip

     elif 'play music' in query: #this function use to play music
        music_dir = 'E:\\ved\\college projects\\python\\jarvis\\music'   
        songs = os.listdir(music_dir)   
        print(songs)               
        os.startfile(os.path.join(music_dir, songs[0]))

     elif 'the time' in query:  # this function id use to see time
        strtime = datetime.datetime.now().strftime("%H:%M:%S")
        print(strtime)
        speak(f"Sir, the time is {strtime}")
      
     elif 'the date' in query:  # this function is use to see real time date
        t_date = datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata')).strftime("%d %B, %Y")
        print(t_date)
        speak(f"sir, the date is {t_date}")
     # write changes in codePath after unzip

     elif 'open code' in query:  # this function is use to open given below apps 
        codePath = "C:\\Users\\HP\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
        os.startfile(codePath)
     elif 'open office' in query:
        officePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\OpenOffice 4.1.9\\OpenOffice.lnk"
        os.startfile(officePath)

     elif 'email to siri' in query: # this function is use to send email with it's subject
         try:
             speak("What should I say?")   
             content = takeCommand()
             to = d
             sendEmail(to, content)
             speak("Email has been send!")
         except Exception as e:
             print(e)
             speak("Sorry sir, I am not able to send this message")
     elif 'shutdown' in query:
        speak("do you really? want to shutdown your system")
        reply = takeCommand()
        if 'yes' in reply:
           os.system('shutdown /s /t 1')
        else:
           Break
     elif 'restart' in query:
        speak("do you really? want to restart your system")
        reply = takeCommand()
        if 'yes' in reply:
           os.system('shutdown /r /t 1')
        else:
           Break
     elif 'log out' in query:
        speak("do you really? want to logout your system")
        reply = takeCommand()
        if 'yes' in reply:
           os.system('shutdown -1')
        else:
           Break

     elif 'exit' in query:
        quit()
