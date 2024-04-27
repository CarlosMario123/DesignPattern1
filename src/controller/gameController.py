from src.view.frames.Game import Game
from src.models.personaje.Personaje import Personaje
from src.logicGame.Combat import Combat
class GameController():
    def __init__(self,route = None):
        self.router = route
        self.combat = None
        self.personaje = Personaje(10,"sonic",2)
        self.view = None
        
    def getView(self,msg=None):
        print("Game",msg)
        self.combat = Combat(self.personaje,msg)
        self.view = Game(controller=self)
        return self.view
    
    def eventCombat(self):
        print("Realizando el combate")
        self.combat.luchar()
        
    
    
    
          