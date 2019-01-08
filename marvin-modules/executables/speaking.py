# Speak file
import sys
from os import path
sys.path.insert(0, path.join(path.dirname(path.abspath(__file__)), 'marvin-modules')) # make env marvin-modules folder in path for pip installed libraries
import speak as marvin_speak

marvin_speak.say(str(sys.argv[1])) # speak
