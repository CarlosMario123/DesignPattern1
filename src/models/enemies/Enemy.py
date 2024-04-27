class Enemy():#procedemos a crear una interfaz enemigo
    def __init__(self, life:int, damage:int, points:int,name:str):
        self.life = life
        self.damage = damage
        self.points = points
        self.name = name

    def attack(self):
        return self.damage
        
            
            

        
    
    
    
    