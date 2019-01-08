try:
    # for Python2
    import Tkinter as tk
except ImportError:
    # for Python3
    import tkinter as tk

from gui_pages import *

LARGE_FONT = ("Verdana", 30)

class MarvinGuiMain(tk.Tk):

    def __init__(self, *args, **kwargs):
        # Initialize TK
        tk.Tk.__init__(self, *args, **kwargs)

        # Create container
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand="True")

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, SettingsPage, MainPage):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)


    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
