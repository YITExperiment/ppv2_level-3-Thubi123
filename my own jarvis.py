import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
import os


listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()



def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talk("Good morning Thubi")
    elif hour>=12 and hour<18:
        talk('good afternoon Thubi')
    else:
        talk("good evening Thubi")
    talk(" Thubi nanthaan, jarvis ,  please, tell me how can i help you")

if __name__ == "__main__":
     wishme()
     
         

def get_command():
    try:
        with sr.Microphone() as source:
            print("listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "stackoverflow" in command:
                command = command.replace("stackoverflow","")
                
    except:
        pass
    return command

def run_assistant():
    command = get_command()
    print(command)
    if 'play' in command:
        song = command.replace("play",' ')
        talk("Thubi, here is your"+ song)
        pywhatkit.playonyt(song)
        print("Thubi Playing songs")

    elif "time" in command:
        time = datetime.datetime.now().strftime("%H : %M %p")
        talk("Thubi Now time is "+ time)

    elif "open my favourite" in command:
        webbrowser.open("https://www.youtube.com/")
    elif "open google" in command:
        webbrowser.open("https://www.google.com/")
    elif "open facebook" in command:
        webbrowser.open("https://www.google.com/search?q=facebook&oq=&aqs=chrome.0.35i39i362l8.24441354j0j15&sourceid=chrome&ie=UTF-8")
    elif "open my channel" in command:
        webbrowser.open("https://www.youtube.com/channel/UC4Tw2Bjm7_RFAc06sSD9iXg")
    elif "open my mail" in command:
        webbrowser.open("https://mail.google.com/mail/u/0/?ogbl#inbox")
    elif "open visual studio" in command:
        codepath="C:\\Users\\Acer\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(codepath)
    
    elif "tell me about" in command:
        about = command.replace("tell me about","")
        info = wikipedia.summary(about,2)
        print(info)
        talk("Thubi according to wikipedia")
        talk(info)
    elif "joke" in command:
        talk(pyjokes.get_joke())

    elif "hi " in command:
        talk("hello ,Thubi ")
    elif "your name" in command:
        talk("my name is jarvis ")
    elif "thank you" in command:
        talk("welcome ,thubi, i will see you ,later ")
    
    


    
    else:
        talk("Thubi ,soory i can't understand tell me again")


while True:
    run_assistant()