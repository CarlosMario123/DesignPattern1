from typing import List
from src.models.factory.FactoryEnemies import FactoryEnemy
from src.models.enemies.Enemy import Enemy
from src.models.enemies.ChoiseEnemies import ChoiseEnemie
import random

class FactoryRandomEnemy(FactoryEnemy):
    def createEnemies(self) -> List[Enemy]:
        num_enemies = random.randint(1,6)
        enemies:List[Enemy] = []
        for _ in range(num_enemies):
            enemies.append(ChoiseEnemie().choiseEnemyByNumber(random.randint(1,2)))
        return enemies    
            