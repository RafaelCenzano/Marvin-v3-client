# env imports
from os import path
from platform import system as platform
from marvinenv.lib.sitepackages.gtts import gTTS
from marvinenv.lib.sitepackages.playsound import playsound

def gtts_speak(tts):
    speach = gTTS(text = tts, lang = 'en-uk')
    speach.save('Speak.mp3')
    if platform() == 'Windows':
        playsound('Speak.mp3')
    else:
        proc = Popen(['mpg321 Speak.mp3'], stdout = PIPE, stderr = PIPE, shell = True)
        (out, err) = proc.communicate()