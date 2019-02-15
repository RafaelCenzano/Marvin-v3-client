# env imports
import sys
from os import path
sys.path.insert(0, path.join('marvin-env','lib','site-packages')) # make env sitepackages folder in path for pip installed libraries

# marvin imports
from gtts import gTTS # gtts for text to speech
from playsound import playsound # play sounds for windows gtts


class gttsSpeak:

    def __init__(self):
        pass

    def say(self, tts):
        speach = gTTS(text = spokenString, lang = 'en-uk') # create string into mp3 file using gtts
        speach.save('Speak.mp3') # save gtts audio as Speak.mp3
        if system() == 'Windows':
            playsound('Speak.mp3')
        else:
            proc = Popen(['mpg321 Speak.mp3'], stdout = PIPE, stderr = PIPE, shell = True) # Popen command with terminal command arguments
            (out, err) = proc.communicate() # opening speak file
