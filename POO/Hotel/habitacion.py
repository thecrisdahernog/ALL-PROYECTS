import os
os.system('cls')

class Habitacion:
    def __init__(self,numero, precio_noche):
        self.numero = numero
        self.precio_noche = precio_noche
        
    def mostrar_info(self):
        print("Habitacion: ", self.numero)
        print("Precio por noche: ", self.precio_noche)
        print("-----------------------")