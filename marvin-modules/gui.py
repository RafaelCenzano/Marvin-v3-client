try:
    # for Python2
    import Tkinter as tk
    import ttk
except ImportError:
    # for Python3
    import tkinter as tk
    from tkinter import ttk


LARGE_FONT = ("Verdana", 30)


class SeaofBTCapp(tk.Tk):

    def __init__(self, *args, **kwargs):
        # Initialize TK
        tk.Tk.__init__(self, *args, **kwargs)

        # Create container
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand="True")

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, PageOne):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)


    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()


class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text='Visit Page 1',
                            command=lambda: controller.show_frame(PageOne))
        button1.pack()

class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One", font=LARGE_FONT)
        label.pack(pady=10, padx=10)

        button1 = ttk.Button(self, text='Back to Start Page',
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

app = SeaofBTCapp()
app.mainloop()
