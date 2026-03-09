class Vehiculo:
    def __init__(self, marca, capacidad_tanque):
        self.marca = marca
        self._capacidad_tanque = capacidad_tanque
        
    def mostrar_info(self):
        print("Vehiculo marca: ", self.marca)
        
    def calcular_autonomia(self):
        pass