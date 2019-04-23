from modules.gui.gui_main import MarvinGuiMain

gui = MarvinGuiMain()
gui.title("Marvin Virtual Assistant")
gui.lift()
gui.attributes("-topmost", True)
gui.focus_set()
gui.focus_force()
gui.after(1, lambda: gui.focus_force())