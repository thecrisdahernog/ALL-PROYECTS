import os
os.system('cls')

from Nave_Espacial import Nave_espacial

class Crucero(Nave_espacial):
    def __init__(self, nombre, vida, ataque, escudo):
        super(). __init__(nombre, vida, ataque)
        self.escudo = escudo   
        
    def recibir_daño(self,cantidad):
        if self.escudo < 0:
            self.vida -= cantidad - self.escudo
            print(f"GRacias a su escudo la nave {self.nombre} solo recibe {cantidad - self.escudo} de daño")
        else: 
            self.vida -= cantidad
            print(f"La nave no cuenta con escudo y recibe {cantidad} de daño")