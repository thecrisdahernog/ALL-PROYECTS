import os
os.system('cls')

from habitacion import Habitacion

class Habitacion_suite(Habitacion):
    def __init__(self, numero, precio_noche, tiene_jacuzzi):
        super().__init__(numero, precio_noche)
        self.tiene_jacuzzi = tiene_jacuzzi
        
    def descripcion(self):
        if self.tiene_jacuzzi:
            print("Habitacion suite con jacuzzi")
        else:
            print("Habitacion suite sin jacuzzi")