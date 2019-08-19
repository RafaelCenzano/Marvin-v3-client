from modules.gui.gui_manager import gui
import sys
from os import path
from os import system as terminal
from platform import system as platform


# make env sitepackages folder in path for pip installed libraries
sys.path.insert(0, path.join('marvin-env', 'lib', 'site-packages'))
from tests.test_manager import test_manager


if platform() == 'Darwin':  # How Mac OS X is identified by Python
    terminal('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')


gui.mainloop()
