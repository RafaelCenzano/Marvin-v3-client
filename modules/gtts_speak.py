# env imports
import sys
from os import path
sys.path.insert(0, path.join('marvin-env','lib','site-packages')) # make env sitepackages folder in path for pip installed libraries

# marvin imports
from gtts import gTTS # gtts for text to speech
from playsound import playsound # play sounds for windows gtts

def gtts_speak(tts):
    speach = gTTS(text = tts, lang = 'en-uk')
    speach.save('Speak.mp3')
    if system() == 'Windows':
        playsound('Speak.mp3')
    else:
        proc = Popen(['mpg321 Speak.mp3'], stdout = PIPE, stderr = PIPE, shell = True)
        (out, err) = proc.communicate()