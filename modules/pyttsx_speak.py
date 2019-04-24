# env imports
import sys
from os import path
sys.path.insert(0, path.join('marvin-env','lib','site-packages')) # make env sitepackages folder in path for pip installed libraries

# marvin imports
import pyttsx3 # run pyttsx3

def pyttsx_speak(self, tts): # function to speak with engine
    engine = pyttsx3.init()
    engine.say(tts) # que tts data
    engine.runAndWait() # speak text
