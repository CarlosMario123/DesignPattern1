#clase que nos permitira selecionar uno de las factory
from src.models.factory import FactoryRandomEnemies,FactoryGombas
from src.models.factory.FactoryEnemies import FactoryEnemy

class ChoiseFactory():
    def choiseModeEnemies(self,mode:str)->FactoryEnemy:
        modeGame = {
            "easy":FactoryGombas.FactoryGomba(),
            "random":FactoryRandomEnemies.FactoryRandomEnemy()
        }
        
        if not modeGame[mode]:
            raise ValueError("Modo de juego no válido: {}".format(mode))
        return modeGame[mode]    