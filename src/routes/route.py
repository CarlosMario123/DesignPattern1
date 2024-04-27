from src.controller.gameController import GameController
from src.controller.indexController import indexController
from src.view.ControllerView import ControllerView

class Route():
    def __init__(self):
        self.routes = {
        "index":indexController,
        "game":GameController
        }
        self.controllerView = ControllerView()
        
    def moveTo(self,ruta:str,msg = None):
        #como podemos ver podemos pasar mensaje en las rutas para tener comunicacion con las vistas vistas
        self.controllerView.change_view(self.routes[ruta](route=self).getView(msg=msg))
    
        

    
    
    
    
    