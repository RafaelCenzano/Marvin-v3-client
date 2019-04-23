try:
    # for Python3
    import tkinter as tk
    from tkinter import ttk

except ImportError:
    # for Python2
    import Tkinter as tk
    import ttk

LARGE_FONT = ("Verdana", 30)

class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Marvin Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text='Settings',
                            command=lambda: controller.show_frame(SettingsPage))
        button1.pack()

        button2 = ttk.Button(self, text='Start',
                            command=lambda: controller.show_frame(MainPage))
        button2.pack()

class SettingsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Settings", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text='Back to Start Page',
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

class MainPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text='Back to Start Page',
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()
