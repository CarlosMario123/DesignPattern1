import tkinter as tk

class MyPerson(tk.Label):
    def __init__(self, master=None, **kwargs):
        tk.Label.__init__(self, master, **kwargs)
        self.place(x=10, y=70)
        self.doConfig()

    def doConfig(self):
        file = "C:/Users/car06/OneDrive/Escritorio/PY/patternDesing/src/img/sonic.png"   # Ruta de la imagen
        
        # Cargar la imagen usando PhotoImage de Tkinter
        self.image = tk.PhotoImage(file=file)
        
        # Configurar la imagen en el widget Label y establecer su posición
        self.config(image=self.image)
