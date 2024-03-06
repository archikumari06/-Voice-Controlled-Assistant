import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib

engine= pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >=0 and hour<=12:
        speak("Good Morning my dear friend")
    elif hour >=12 and hour < 18:
        speak("Good Morning my dear friend")
    else:
        speak("Good evening my dear friend")
    speak("Let me know how can I help you, What are you looking for ?")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening to you Archi.....")
        r.pause_threshold = 1
        audio =r.listen(source)
    try:
        print("Recognizing your voice....")
        query =r.recognize_google(audio,language='en-in')
        print(f"My dear friend you said :{query}\n")
    except Exception as e:
        print("Archi say that again please....")
        return "None"
    
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('archikumari@gmail.com','123456')
    server.sendmail('archikumari@gmail.com',to,content)
    server.close()

   
   

if __name__ =='__main__':
    wishme()


    while True:
        query = takecommand().lower()

        if 'open wikipedia' in query:
            speak('Searching wikipedia....')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        if 'open notepad' in query:
            npath ="C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath) 


        elif 'open paint' in query:
            npath = "C:\\Windows\\system32\\mspaint.exe" 
            os.startfile(npath)
        
        elif 'open Youtube' in query:
            webbrowser.open('youtube.com')
         
        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'tell me the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"My dear friend,the time is{strTime}")

        elif 'open linkedIn' in query:
            webbrowser.open('https://www.linkedin.com/in/archi-kumari-555a451a4/') 

        elif 'email to other friend' in query:
            try:
                speak("what should i send?")
                content = takecommand()
                to ="kumariarchi@gmail.com" 
                sendEmail(to,content)
                speak("Mail sent sucessfully")

            except Exception as e:
                print(e)
                speak("My dear friend ...I am unable to send the email...Please address the error")
                               
          

