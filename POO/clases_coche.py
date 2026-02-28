import os
os.system('cls')
class Auto:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.velocidad = 0
        
    def acelerar(self, aumento):
        self.velocidad += aumento
        print(f"{self.marca} - {self.modelo} acelera. velocidad actual {self.velocidad} km/h")
        
    def frenar(self, reduccion):
        self.velocidad -= reduccion 
        if self.velocidad < 0:
            self.velocidad = 0
        print(f"{self.marca} - {self.modelo} frena. velocidad actual {self.velocidad} km/h")
        
    def mostrar_velocidad(self):
        print(f"{self.marca} - {self.modelo}.  velocidad actual {self.velocidad} km/h")
        
auto1 = Auto("Toyota", "Supra")
auto2 = Auto("Renault", "Twingo")
auto3 = Auto("Ford", "Mustang")
auto4 = Auto("Ferrari", "SF90")

auto1.acelerar(40)
auto2.acelerar(12)
auto3.acelerar(38)
auto4.acelerar(55)

auto1.frenar(20)
auto3.frenar(20)
auto4.frenar(20)
auto2.acelerar(20)

print("velocidades final: ")
auto1.mostrar_velocidad()
auto2.mostrar_velocidad()
auto3.mostrar_velocidad()
auto4.mostrar_velocidad()
