from src.models.enemies import Gomba,Turtle
class ChoiseEnemie():
    def choiseEnemie(self,name:str):
        choice = {
            "Gomba":Gomba.Gomba,
             "Turtle":Turtle.Turtle
        }
        return choice[name]
    def choiseEnemyByNumber(self,number:int):
        choice = {
            1:Gomba.Gomba,
            2:Turtle.Turtle
        }
        return choice[number] 
        