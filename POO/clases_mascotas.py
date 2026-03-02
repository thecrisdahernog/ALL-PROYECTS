import os
os.system('cls')

class Mascota:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hambre = 20
        self.felicidad = 100
        self.energia = 50
        
    def comer (self):
        self.hambre -= 20        
        self.energia += 5
        print(f"{self.nombre} ha comido y se siente mejor.")
        
    def jugar (self):
        self.hambre += 10
        self.felicidad += 20
        self.energia -= 15
        print(f"{self.nombre} ha jugado y se siente feliz.")
        
    def dormir (self):
        self.hambre += 5
        self.felicidad += 5
        self.energia += 30
        print(f"{self.nombre} ha dormido y se siente descansado.")
        
    def info (self):
        print(f"Nombre: {self.nombre}")
        print(f"Hambre: {self.hambre}")
        print(f"Felicidad: {self.felicidad}")
        print(f"Energia: {self.energia}")
        
    def opciones (self):
        print("""
                Selecciona una de las siguientes acciones:""")
        print("1. Comer")
        print("2. Jugar")
        print("3. Dormir")
        print("4. Ver información")
        if self.opciones == "1":
            self.comer()
            self.info()
        elif self.opciones == "2":
            self.jugar()
            self.info()
        elif self.opciones == "3":
            self.dormir()
            self.info()
        elif self.opciones == "4":
            self.info()
        else:
            print("Opción no válida. Por favor, selecciona una opción del 1 al 4.")
        
        
Mascota1 = Mascota("Buddy")