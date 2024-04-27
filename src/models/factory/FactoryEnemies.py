from abc import ABC,abstractmethod
from src.models.enemies.Enemy import Enemy
from typing import List #para trabajar con lista
class FactoryEnemy(ABC):
    @abstractmethod
    def createEnemies(self)->List[Enemy]:
        pass
