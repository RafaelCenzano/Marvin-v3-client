# Speak file
import sys
from modules.pyttsx_speak import pyttsx_speak

pyttsx_speak(str(sys.argv[1:]))
