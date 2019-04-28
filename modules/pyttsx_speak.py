# env imports
from os import path
from marvinenv.lib.sitepackages import pyttsx3

def pyttsx_speak(tts): # function to speak with engine
    engine = pyttsx3.init()
    engine.say(tts) # que tts data
    engine.runAndWait() # speak text
