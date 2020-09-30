import speech_recognition as sr
import pattern # own module class
import random
import pyttsx3  # 7, 11, 17, 18, 27, 29, 34, 41*,  ( Female voices )
import datetime
import webbrowser
import wikipedia
import osascript
import os

pt = pattern.Patterns()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[41].id)
r = sr.Recognizer()


def sofispeak(query):
    engine.say(query)
    print("Sophie : " + query)
    engine.runAndWait()


def user_say():
    with sr.Microphone() as source:
        try:
            print( "Sophie : Listening...")
            r.energy_threshold = 600
            text = r.recognize_google(r.listen(source))
            print("You    : " + text)
            return text
        except:
            # sofispeak("I can't recognize. Say again")
            return ""



def welcome():
    hour = int(datetime.datetime.now().hour)
    if hour < 12:
        sofispeak("Hello Sir, Good Morning. How can I help you?")
    elif hour >= 12 and hour < 17:
        sofispeak("Hello Sir, Good Afternoon. How can I help you?")
    else:
        sofispeak("Hello Sir, Good Evening. How can I help you?")


# Main part
while True:
    with sr.Microphone() as source:
        try:
            print( "Sophie : Sleeping...")
            r.energy_threshold = 700
            text = r.recognize_google(r.listen(source))
            print("You    : " + text)
        except:
            text = ""

    

    if 'hi sophie' in text.lower() or 'hi sofi' in text.lower():
        text = ""
        welcome()
        said = user_say().lower()
        volume = 100
        while True:
            if 'who are you' in said:
                sofispeak("An AI assistant build with Python.")

            elif 'what is your name' in said:
                sofispeak("My name is Sophie.")

            # elif 'how are you' in said:
            #     sofispeak("I'm fine Sir. What about you?")

            elif said in pt.how_are_you:
                sofispeak(random.choice(pt.how_are_you_reply))

            elif 'fine' in said:
                sofispeak("Good. How can i help you Sir?")

            elif 'the time' in said:
                sofispeak("Sir the time is " + datetime.datetime.now().strftime("%H:%M:%S"))

            elif 'thank you' in said:
                sofispeak("No problem Sir. Tell me anything.")
            
            elif 'who is' in said or 'wikipedia' in said or 'what is' in said:
                said = said.replace('who is','')
                said = said.replace('what is','')
                said = said.replace('wikipedia','')
                print( "Sofi : Searching...")
                sofispeak("According to Wikipedia " + wikipedia.summary(said, sentences=1))

            elif "goodbye" in said or "bye" in said:
                hour = int(datetime.datetime.now().hour)
                if hour >= 20:
                    sofispeak("Ok Sir, good night. See you soon.")
                    break
                else:
                    sofispeak("Ok Sir, good bye. See you soon.")
                    break

                    

            elif "calculate" in said:
                said = said.replace("calculate", "")
                said = said.replace("by", "")
                said = said.replace("multiply", "*")
                said = said.replace("x", "*")
                numbers1 = said.split()
                numbers2 = []

                for i in numbers1:
                    try:
                        numbers2.append(int(i))
                    except:
                        numbers2.append(i)
                
                total = numbers2[0]
                numbers2.remove(numbers2[0])

                while True:
                    if len(numbers2) == 0:
                        break

                    if "+" in numbers2[0] or "plus" in numbers2[0]:
                        numbers2.remove('+')
                        total += numbers2[0]
                        numbers2.remove(numbers2[0])

                    elif "-" in numbers2[0]:
                        numbers2.remove('-')
                        total -= numbers2[0]
                        numbers2.remove(numbers2[0])

                    elif "*" in numbers2[0]:
                        numbers2.remove('*')
                        total *= numbers2[0]
                        numbers2.remove(numbers2[0])

                    elif "divide" in numbers2[0] or "divided" in numbers2[0]:
                        try:
                            numbers2.remove('divide')
                        except:
                            pass
                        try:
                            numbers2.remove('divided')
                        except:
                            pass
                        total /= numbers2[0]
                        numbers2.remove(numbers2[0])

            
                sofispeak(str(total))

            elif "open youtube" in said:
                sofispeak("Opening youtube..")
                webbrowser.open("https://youtube.com")
            
            elif "open gmail" in said:
                sofispeak("Opening gmail")
                webbrowser.open("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
            
            elif "open facebook" in said:
                sofispeak("Opening facebook")
                webbrowser.open("https://facebook.com")

            elif "open lpu admission" in said:
                sofispeak("Opening LPU admission dashboard")
                webbrowser.open("https://admission.lpu.in/StudentDashboard")

            elif "visit my site" in said:
                sofispeak("Visiting your website")
                webbrowser.open("https://rajmazumder.xyz")

            elif "search on youtube" in said:
                said = said.replace("search on youtube","")
                sofispeak("Searching...")
                webbrowser.open("https://www.youtube.com/results?search_query=" + said)

            elif "set direction" in said:
                said = said.replace("set direction","")
                place = said.split("to")
                said = said.replace("to","")
                sofispeak("Setting direction...")
                webbrowser.open("https://www.google.com/maps/dir/{}/{}".format(place[0], place[1]))

            elif "open whatsapp" in said:
                sofispeak("Opening WhatsApp")
                os.system("open /Applications/WhatsApp.app")

            elif "reduce volume" in said or "decrease volume" in said:
                volume -= 20
                osascript.osascript("set volume output volume {}".format(volume))

            elif "increase volume" in said:
                volume += 20
                osascript.osascript("set volume output volume {}".format(volume))


            elif "new python project" in said:
                said = said.replace("new python project", "")
                os.mkdir("/Volumes/All files/python/{}".format(said))
                with open("/Volumes/All files/python/{}/{}.py".format(said,said), 'w') as w:
                    pass
                os.system("code /Volumes/All\ files/python/\{}".format(said))

            elif "set a reminder on" in said:
                said = said.replace("set a reminder on", "")


            

            said = user_say().lower()
