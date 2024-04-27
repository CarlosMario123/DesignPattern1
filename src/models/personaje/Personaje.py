class Personaje():
    def __init__(self,vida:int,name:str,damage:int):
        self.vida = vida
        self.name = name
        self.damage = damage
    def incrementDamage(self,damage:int):
        self.damage += damage
    def decrementLife(self,life:int):
        self.vida -= life
    