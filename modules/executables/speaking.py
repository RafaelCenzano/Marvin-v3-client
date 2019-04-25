# Speak file
import sys
from os import path
sys.path.insert(0, path.join(path.dirname(path.abspath(__file__)), 'marvin-modules')) # make env marvin-modules folder in path for pip installed libraries
from modules.pyttsx_speak import pyttsx_speak

pyttsx_speak(str(sys.argv[1:]))
