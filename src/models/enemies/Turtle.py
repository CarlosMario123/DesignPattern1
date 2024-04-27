from src.models.enemies.Enemy import Enemy
class Turtle(Enemy):#hacemos uso de la clase Enemy
    def __init__(self):
        super().__init__(7,7,3,"Turtle")
    def attack(self):
        return super().attack() 
