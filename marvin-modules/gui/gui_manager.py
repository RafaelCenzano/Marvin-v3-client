import sys
from os import path
sys.path.insert(0, path.join(path.dirname(path.abspath(__file__)), 'marvin-modules', 'gui')) # make env marvin-modules folder in path for pip installed libraries
from gui_main import MarvinGuiMain

gui = MarvinGuiMain()
gui.title("Marvin Virtual Assistant")
gui.lift()
gui.attributes("-topmost", True)
