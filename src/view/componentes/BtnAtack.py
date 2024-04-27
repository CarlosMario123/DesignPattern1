import tkinter as tk

class BtnAtack(tk.Button):
    def __init__(self):
        super().__init__()
        self.config(text="Atacar", width=20, height=2)
        self.place(x=10, y=490)
    
    def setClick(self,callback):
        self.config(command=callback)
        
