import os
os.system('cls')

from Nave_Espacial import Nave_espacial

class Caza(Nave_espacial): 
    def __init__(self, nombre, vida, ataque, velocidad):
        super().__init__(nombre, vida, ataque)
        self.velocidad = velocidad
        self.maniobra = False
        
    def maniobra_evasiva(self):
        self.maniobra = True
        print(f"{self.nombre} ha realizado maniobras evasivas)")
    
    def recibir_daño(self,cantidad):
        if self.maniobra:
            self.vida -= cantidad - 10
            print(f"La nave {self.nombre} realizo una maniobra evasiva y solo recibe {cantidad -10} de daño")
        else:
            self.vida -= cantidad
            print(f"la nave {self.nombre} no pudo realizar maniobras evasivas y recibe {cantidad} de daño")