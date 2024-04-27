import tkinter as tk
from src.models.personaje.Personaje import Personaje

class MyLife(tk.Label):
    def __init__(self,personaje:Personaje):
        super().__init__()
        self.personaje = personaje
        
        
        
        
        self.config(text=f"vida:{str(self.personaje.vida)}",font=("Helvetica", 16))
        self.place(x=0, y=0)  

    def set_text(self, text):
        self.config(text=text)
        
    def actualizar(self):
        print(self.personaje.vida)
        self.config(text=f"vida:{str(self.personaje.vida)}")
