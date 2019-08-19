from modules.gui.gui_manager import gui
from os import system as terminal
from platform import system as platform


if platform() == 'Darwin':  # How Mac OS X is identified by Python
    terminal('''/usr/bin/osascript -e 'tell app "Finder" to set frontmost of process "Python" to true' ''')


gui.mainloop()
