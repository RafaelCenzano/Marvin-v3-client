import sys
from os import path
sys.path.insert(0, path.join('marvin-env','lib','site-packages')) # make env sitepackages folder in path for pip installed libraries
sys.path.insert(0, path.join('marvin-modules')) # make env marvin-modules folder in path for pip installed libraries
sys.path.insert(0, path.join('marvin-modules','gui')) # make env marvin-modules folder in path for pip installed libraries
from gui_manager import gui

gui.mainloop()

# Sounds, Terminal Control
# linux sounds amixer sset 'Master' 50% change percent
# mac sounds  osascript -e "set Volume 0" Lowest
# mac sounds  osascript -e "set Volume 3.5" Middle
# mac sounds  osascript -e "set Volume 7" Max
