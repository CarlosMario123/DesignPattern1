#esta es una clase que nos permitira generar gombas de manera aleaotria como un maximo de 5 gombas
from typing import List
from src.models.factory.FactoryEnemies import FactoryEnemy
from src.models.enemies.Enemy import Enemy
from src.models.enemies.ChoiseEnemies import ChoiseEnemie
import random
class FactoryGomba(FactoryEnemy):
    def createEnemies(self) -> List[Enemy]:
        enemies = []
        num_enemies =  random.randint(1,5)
        for _ in range(num_enemies):
            enemies.append(ChoiseEnemie().choiseEnemie("Gomba"))
        return enemies
        
    