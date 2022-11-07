from email.mime import audio
import re as sr

import pyttsx3
#initialize the recognizer
r= sr.Recognizer()
# function to convert text to 
# speech
def SpeakText(command):
    #initializer the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()
    # loop infinitely for user to
    # speak
    while(1):
        # Exception handling to handle
        # exception at the runtime
        try:
            #use the microphone as source for input.
             with sr.Microphone ()as source:
                r.adjust_for_ambient_noise(source)
                MyText = r.recognize_google(audio)
                MyText = MyText.lower()
                print("Did you say "+MyText)
                SpeakText (MyText)
        except sr.RequestError as e :
            print("could not request resuits: {0}".format(e))
        except sr.UnknownValueError:
            print("unknown error occured")
