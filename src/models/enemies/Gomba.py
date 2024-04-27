from src.models.enemies.Enemy import Enemy
from src.models.personaje.Personaje import Personaje
class Gomba(Enemy):#hacemos uso de la clase Enemy
    def __init__(self):
        super().__init__(3,5,1,"Gomba")
    def attack(self,personaje:Personaje):
        return super().attack() 
     
        
    
    
    