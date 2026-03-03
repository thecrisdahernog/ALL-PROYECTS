import os
os.system('cls')

from habitacion import Habitacion

class Habitacion_Simple(Habitacion):
    def __init__(self, numero, precio_noche, camas):
        super().__init__(numero, precio_noche)
        self.camas = camas
        
    def descripcion(self):
        print("Habitacion simple con: ", self.camas, "camas")