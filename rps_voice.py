import pyttsx3
import random
import speech_recognition as sr
from playsound import playsound
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
#Audio Spaeaking
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
#Welcome Message
def welcome():
    playsound('start.wav')
    print("Rock-paper-scissor is a quick win-loose game")
    speak("Rock-paper-scissor is a quick win-loose game")
    print("_________Game RULES_________")
    print("___Rock wins over scissor___\n___Scissor wins over paper___\n___Paper wins over rock___")
    print("Are you ready to play the game ? Yes or No ?")
    speak("Are you ready to play the game ? Yes or No ?")
#Taking Input in Voice
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("You have Chosen: ",query)
    except Exception as e:
        print(e)
        print("Say that again please...")
        return takeCommand()
    return query
#Game Process
def gamewin(p1, p2):
    if(p2 == 'rock' or p2 == 'paper' or p2 == 'scissor'):
        if(p1 == p2):
            return None
        elif(p1 == 'rock'):
            if(p2 == 'paper'):
                return True
            elif(p2 == 'scissor'):
                return False
        elif(p1 == 'paper'):
            if(p2 == 'scissor'):
                return True
            elif(p2 == 'rock'):
                return False
        elif(p1 == 'scissor'):
            if(p2 == 'rock'):
                return True
            elif(p2 == 'paper'):
                return False
    else:
        speak("Sorry, we could not recognize your voice.")
        print("Say that again please...")
        play2()          
#Computer Choosing Randomly 
def computer():
    li = ['rock', 'paper', 'scissor']
    return random.choice(li)
#Checking For Winner
def result(a,p1):
    if (a == None):
        print("Computer has Chosen : ",p1)
        print("It's a Tie")
        speak("Its a Tie")
        playsound('tie.wav')
    elif a:
        print("Computer has Chosen : ",p1)
        print("Great !! You Won The Match, Winner Winner Biriyani Dinner.")
        speak("Great !! You Won The Match ,Winner Winner Biriyani Dinner.")
        playsound('win.wav')
        exit()
    else:
        print("Computer has Chosen : ",p1)
        print("You Loose the Match. Better luck next TIme")
        speak("You Loose the Match. Better luck next TIme")
        playsound('loose.wav')

#Gameplay
def play():
    op = takeCommand()
    yes_no=['yes','yeah','yes yes','no','no no']
    if op in yes_no:
        if op in yes_no[0:3]:
            while(True):
                print("Please choose among rock-paper-scissor")
                speak("Please choose among rock-paper-scissor")
                p2 = takeCommand()
                p1=computer()
                result(gamewin(p1, p2),p1)
        elif op in yes_no[3:5]:
            print("OK,see you soon. Have a nice day!")
            speak("OK,see you soon. Have a nice day!")
            exit()
    else:
        speak("Sorry, we could not recognise your voice.")
        print("Are you ready to play the game ? Yes or No ?")
        speak("Are you ready to play the game ? Yes or No ?")
        play()
#if Input-Voice Coudn't Recognised
def play2():
    while(True):
        print("Please choose among Rock-Paper-Scissor")
        speak("Please choose among Rock-Paper-Scissor")
        p2 = takeCommand()
        p1=computer()
        result(gamewin(p1, p2),p1)
#Main Function
welcome()
play()
