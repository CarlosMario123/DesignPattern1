import tkinter as tk

class MainWindow(tk.Tk):
    def __init__(self,controller):
        super().__init__()
        self.controller = controller
        self.title("Ventana Principal")
        self.geometry("600x600")
        self.create_button("easy")
        self.create_button("random")

    def create_button(self, mode):
        btn = tk.Button(self, text=mode, command=lambda m=mode: self.openGame(m))
        btn.pack()

    def openGame(self, mode):
        self.destroy()
        self.quit()
        self.controller.choiseModeGame(mode)
