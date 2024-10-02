# making a chatbot using python
import pyttsx3
import speech_recognition as sr 
import webbrowser
import datetime 

def sptext(): # speech_recognisation module returns our speech in the form of text
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print ("listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print ("recognising")
            data = recognizer.recognize_google(audio)
            print (data)
            return data
            
        except sr.UnknownValueError:
            print ("not understandable")


def speechtx(x): 
#pyttsx3 returns our command in the form of speech we can set the voice in the form of female voice or male voice but we have to download it first
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    rate = engine.getProperty('rate')
    engine.setProperty('rate',150)
    engine.say(x)
    

if __name__ == '__main__': # this function will import only the most required items of the module and will make the upper function a seperate programme and this function a seperate programme

    if sptext().lower() == "hey friday":
        data1 = sptext().lower()

    if "what is your name" in data1:
            name = 'my name is friday'
            speechtx(name)
    elif "what is your age" in data1:
            age = "i dont have any age but my creater raghav's age is 14"
            speechtx(age)
    elif 'what is the time right now' in data1:
            time = datetime.datetime.now().strftime("%I%M%p")
            speechtx(time)
    elif "what is your creators name" in data1:
            creater = "my creators name is raghav"
            speechtx(creater)
    elif "what project are we working on" in data1:
            answer = "we are working on making me better and later on making another chatbot like me"
            speechtx(answer)
    elif "friday open youtube" in data1:
          webbrowser.open("https://www.youtube.com")


        
    