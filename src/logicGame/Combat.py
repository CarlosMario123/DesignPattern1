from src.models.personaje.Personaje import Personaje
from src.models.choiseFactory import ChoiseFactory
class Combat():
    def __init__(self,personaje:Personaje,modeGame:str):
        self.personaje = personaje
        self.modeGame = ChoiseFactory().choiseModeEnemies(modeGame)
    def luchar(self):
        self.personaje.decrementLife(2)
        