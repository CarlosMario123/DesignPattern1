import tkinter as tk

class BtnHuir(tk.Button):
    def __init__(self, master=None,**kwargs,):
        tk.Button.__init__(self, master, **kwargs)
        self.config(text="Huir", width=20, height=2)
        self.place(x=400, y=490)
    
    def setClick(self,callback):
        self.config(command=callback)