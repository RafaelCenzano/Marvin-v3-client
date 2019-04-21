from marvin - modules.gui.gui_manager import gui
import sys
from os import path
# make env sitepackages folder in path for pip installed libraries
sys.path.insert(0, path.join('marvin-env', 'lib', 'site-packages'))


gui.mainloop()
