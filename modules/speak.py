from modules.gtts_speak import gtts_speak
from modules.network import internet_on
from sys import executable as python_path
from os import system as terminal

def say(tts):
    check_connection = internet_on()
    if check_connection == True and speak_type == 1:
    	gtts_speak(tts)
    elif check_connection == False and speak_type == 2:
    	terminal(f'{python_path} executables/speaking.py {tts}')