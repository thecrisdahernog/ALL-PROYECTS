import os
import random
os.system('cls')

class Nave_espacial:
    def __init__(self, nombre, vida, ataque):
        self.nombre = nombre
        self.vida = 100
        self.ataque = ataque
        
    def disparar(self, Objetivo):
        Objetivo.vida -= self.ataque
        print(f" {self.nombre} dispara a {Objetivo.nombre} y le quita {self.ataque} de vida, la vida restante de {Objetivo.nombre} es {Objetivo.vida}")
        critico = random.randint(1,10+1)
        if critico != 10:
            Objetivo.recibir_daño(self.ataque)
        else:
            Objetivo.recibir_daño(self.ataque + 10)
            print("¡Disparo critico!")
        
    def recibir_daño(self,cantidad):
        self.vida -= cantidad
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nombre} ha recibido {cantidad} de daño, su vida restante es {self.vida}")
        
    def estado_vida(self):
        if self.vida == 0:
            print(f"la nave {self.nombre} ha sido destruida")
        elif self.vida < 0:
            self.vida = 0
            print(f"la nave {self.nombre} ha sido destruida")
            
    def reparar(self,cantidad):
        self.vida += cantidad + 15
        if self.vida > 100:
            self.vida = 100
        print(f"{self.nombre} la nave ha sido reparada y ahora tiene {self.vida} de vida")
        
        
    def mostrar_estado(self):
        print(f"nombre : {self.nombre}\nvida : {self.vida}\nAtaque: {self.ataque}")
