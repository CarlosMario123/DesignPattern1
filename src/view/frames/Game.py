import tkinter as tk
from src.view.componentes import MyLabel, MyPerson, BtnAtack, BtnHuir

class Game(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.title("Game learn factory")
        self.geometry("600x600")
        self.controller = controller
        self.init_ui()

    def init_ui(self):
        self.my_life_label = MyLabel.MyLife(self.controller.personaje)
        self.my_person = MyPerson.MyPerson(self)
        self.btn_atack = BtnAtack.BtnAtack().setClick(self.eventBtnAtack)
        self.btn_huir = BtnHuir.BtnHuir(self)
        
    def eventBtnAtack(self):
        self.my_life_label.actualizar()
        self.controller.eventCombat()
        
        
