import os
os.system('cls')
class Perro:
    def __init__(self, nombre, color, edad):
        self.nombre = nombre
        self.color = color
        self.edad = edad
        
    def ladrar(self):
        return f"¡{self.nombre} dice: guau!"
    
    def correr(self):
        return f"{self.nombre} está corriendo."
    
mi_perro = Perro("Sacha", "Marron", 7)
mi_perro2 = Perro("Jiren", "Blanco", 9)
mi_perro3 = Perro("Terry", "Cafe", 4)
mi_perro4 = Perro("Maluma", "Negro", 4)

print(f"{mi_perro.nombre} y {mi_perro3.nombre} esta ladrando")
print(f"{mi_perro.nombre} ladra")
print(mi_perro.ladrar())
print(f"{mi_perro3.nombre} responde")
print(mi_perro3.ladrar())
print("SE FORMO LA PELEA DE PERROS")
print(mi_perro.ladrar())
print(mi_perro2.ladrar())
print(mi_perro3.ladrar())
print(mi_perro4.ladrar())

