# env imports
import sys
from os import path
sys.path.insert(0, path.join('marvin-env','lib','site-packages')) # make env sitepackages folder in path for pip installed libraries

# marvin imports
import pyttsx3 # run pyttsx3

class Pyttsx3Speak:

    def __init__(self): # initialize engine function
        self.engine = pyttsx3.init() # initialize engine

    def say(self, tts): # function to speak with engine
        self.engine.say(tts) # que tts data
        self.engine.runAndWait() # speak text
