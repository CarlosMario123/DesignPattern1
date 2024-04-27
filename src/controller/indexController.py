from src.view.frames.MainFrame import MainWindow #vista por defecto
from src.models.choiseFactory import ChoiseFactory


class indexController():
    def __init__(self,route = None):
        self.choiseFactory = ChoiseFactory()#uso del modelo Choise 
        self.view = MainWindow(controller=self)
        self.router = route
    def choiseModeGame(self,mode):
        self.view.quit()
        self.router.moveTo("game",mode)
        
    def getView(self,msg=None):
        return self.view