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
        tk.Frame.__init__(self, parent, bg='#191919')
        label = tk.Label(self, text='Marvin Start Page', font=LARGE_FONT, fg='#e2e2e2', bg='#191919')
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text='Settings',
                            command=lambda: controller.show_frame(SettingsPage), highlightbackground='#191919')
        button1.pack()

        button2 = tk.Button(self, text='Start',
                            command=lambda: controller.show_frame(MainPage), highlightbackground='#191919')
        button2.pack()

class SettingsPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#191919')
        label = tk.Label(self, text="Settings", font=LARGE_FONT, fg='#e2e2e2', bg='#191919')
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text='Back to Start Page',
                            command=lambda: controller.show_frame(StartPage), highlightbackground='#191919')
        button1.pack()

class MainPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent, bg='#191919')
        label = tk.Label(self, text="Page One", font=LARGE_FONT, fg='#e2e2e2', bg='#191919')
        label.pack(pady=10, padx=10)

        button1 = tk.Button(self, text='Back to Start Page',
                            command=lambda: controller.show_frame(StartPage), highlightbackground='#191919')
        button1.pack()
