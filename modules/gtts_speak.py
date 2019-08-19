# env imports
from os import path
from platform import system as platform
from marvinenv.lib.sitepackages.gtts import gTTS
from marvinenv.lib.sitepackages.playsound import playsound

os_type = platform()

if os_type == 'Windows':
	def speak_audio():
		playsound('Speak.mp3')
else:
    def speak_audio():
        proc = Popen(['mpg321 Speak.mp3'], stdout = PIPE, stderr = PIPE, shell = True)
        (out, err) = proc.communicate()

def save_audio(tts):
    speach = gTTS(text = tts, lang = 'en-uk')
    speach.save('Speak.mp3')

def gtts_speak(tts):
    save_audio(tts)
    speak_audio()