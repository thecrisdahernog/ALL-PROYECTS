import os
os.system('cls')
class Mago:
    def __init__(self, nombre, nivel, mana):
        self.nombre = nombre
        self.nivel = nivel
        self.mana = mana
        self.vida = 100
        
    def lanzar_hechizos(self, hechizo, ataque, magoObjetivo):
        self.mana -= ataque
        magoObjetivo.vida -= ataque
        print(f"{self.nombre} lanzo un {hechizo}, desgastando su mana en {ataque} % y bajando la vida de su adversario {magoObjetivo}")
        
    def Meditacion(self, Horas):
        self.mana += ((self.nivel * Horas ) / 2)* 3
        print(f"{self.nombre} a meditado {Horas} horas y ha recuperado {((self.nivel * Horas ) / 2)* 3} de mana")
        
    def subir_nivel(self):
        self.nivel +=1
        print(f"{self.nombre} ha subido de nivel, su nivel actual es {self.nivel}")
        
Mago1 = Mago("")