import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import requests
import json
# fetch data is a python file by which we are fatching data we import here as a module
#import fetchdata
import sys

engine= pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices)
engine.setProperty('voice', voices[1].id)
#print(voices[0].id)
engine.setProperty('rate',135)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning to yours complicated day i hope we will make it good for u lets start it")
        # time()
        # intoduce()

    elif(hour==12):
         speak("good Noon  to yours complicated day, u have alerady completed yours half day.I hope we will make it good for u lets start it")
        #  time()
        #  intoduce()
    elif(hour>12 and hour<18):
         speak("good AfterNoon  to yours complicated day, u have alerady completed yours half day.I hope we will make it good for u lets start it")
        #  time()
        #  intoduce()
    else:
         speak("good evening to yours complicated day i hope we will make it good for u lets start it")
        #  time()
        #  intoduce()


def time():
    dt=datetime.datetime.now()
    specal = dt.strftime("%A, %d.%B %Y %I:%M%p")
    #print(dt)
    #print(specal)
    timing ='Today is {0:%A},The {1} is {0:%d}, the {2} is {0:%B}, the {3} is {0:%I:%M%p}'.format(dt,"date","month","time")
    speak(timing)
def intoduce():
    introduction = "oh okay    let me introduce ,who am I  , i am a virtual thing which can do anything for you. you just need to give me instructions what do you want to know mister UTKARSH. "
    choice =" if u are in conflict situation you can choose the function ,   these are listed blow  you just need to say choose"
    speak(introduction)
    speak(choice)
    


def choose():
        speak("we are ready to choose")
        '''
        listed the operated functions
        '''
        functionlist=['wish','intro','time','wikipedia','open youtube','stackoverflow','open gmail','open google','play music','stop']
        speak("you can say ")
        for function in functionlist:
            speak(function)
        speak("you can choose what you want.  now its your turn")

def taskCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold = 1
        # r.energy_threshold = 150
        r.adjust_for_ambient_noise(source,duration=1)
        print("listening....")
        audio= r.listen(source)
        print("listening completed")
    try:
        # print("i think you said"+ r.recognize_google(audio, language="en-in"))
        print("recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print("user said : query= ",query)
        # operations(query)

    except Exception as ex:
        print(ex)
        print("say that again please...")
        return "None"
    except sr.UnknownValueError as identifier:
        print("i could not understand auidio")
    except sr.RequestError as e:
        print("jarvis error: {0}".format(e))
    except sr.WaitTimeoutError:
        print("sorry timeout")
    # else:
    #     data = query
    #     print("inside else",data)
    return query

def operations(userdata):
    # print("we are searching function",userdata)
    if "time" in userdata:
        time()
    elif "wish" in userdata:
        wishMe()
    elif "intro" in userdata:
        intoduce()
    elif "choose" in userdata:
        choose()
    elif 'wikipedia' in userdata:
        wiki(userdata)
    elif 'open youtube' in userdata:
        youtube()
    elif 'google' in userdata:
        google()
    elif 'stackoverflow' in userdata:
        stack()
    elif 'gmail' in userdata:
        mail()
    elif 'music' in userdata:
        music()
    elif 'code' in userdata:
        code()
    elif 'government job' in userdata:
        latestjob()
    elif 'news' in userdata:
        news()
    elif 'send email' in userdata:
        try:
            speak("what should i say?")
            content = taskCommand()
            to = "recivermail@gmail.com"
            email(to,content)
            speak("email has been sent successfully")
        except expression as e:
            print(e)
            speak("we are not able to send your email")

    else:
        if not 'stop' in userdata:
            speak("its not recognizing command")
            speak("give me another option or you can say choose to see my commands")



def wiki(data):
    speak("searching wikipedia...")
    results = wikipedia.summary(data,sentences=2)
    speak("according to wikipedia  ")
    speak(results)

def youtube():
    webbrowser.open("youtube.com")

def google():
    webbrowser.open("google.com")
def stack():
    webbrowser.open("stackoverflow.com")

def mail():
    webbrowser.open("google/gmail.com")
def music():
    music_dir = 'E:\\songs collection\\music'
    songs=os.listdir(music_dir)
    os.startfile(os.path.join(music_dir, songs[0]))
def code():
    codepath = 'C:\\Users\\UTKRASH\\AppData\\Local\\Programs\\Microsoft VS Code\\code.exe'
    os.startfile(codepath)

def email(to,content):
    server = smtplib.SMTP('smtp@gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com' , 'your password') # provide your email account credantial
    server.sendmail('youremail@gmail.com',to,content)
    server.close()

def latestjob():
    reference = os.system('python fetchdata.py')
    if reference==None:
        sys.exit()
def news():

    url = ('http://newsapi.org/v2/top-headlines?''country=us&''apiKey=259a2714912e4f949575ce2b9999ec7d')
    response = requests.get(url)
    data = response.content
    jdata = json.loads(data.decode())
    article=jdata["articles"]
    result=[]
    for item in article:
        title=item["title"]
        result.append(title)

    for i in range(len(result)):
        my_json = json.dumps(result[i])
        speak(my_json)



if __name__ == "__main__":
    speak("welcome  in the virtual world")
    speak("how may i help you?")
    # wishMe()
    while True:
        query = taskCommand().lower()
        operations(query)
        if 'stop' in query:
            speak('okay i m going to sleep')
            break
        query= query.replace(query,"")
    speak("thanks for choosing me")
        
