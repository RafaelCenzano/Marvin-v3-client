from modules.gtts_speak import gtts_speak
from modules.network import internet_on
from sys import executable as python_path
from os import system as terminal
from os import path
from marvinenv.path import marvin_path

def say(tts):
    check_connection = internet_on()
    if check_connection == True and speak_type == 1:
    	gtts_speak(tts)
    elif check_connection == False and speak_type == 2:
    	speaking_executable = path.join(marvin_path,'executables','speaking.py')
    	terminal(f'{python_path} {speaking_executable} {tts}')