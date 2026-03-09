from vehiculo import Vehiculo

class Camion(Vehiculo):
    def __init__(self, marca, capacidad_tanque, consumo_por_litro, carga):
        super().__init__(marca, capacidad_tanque)
        self._consumo_por_litro = consumo_por_litro
        self.carga = carga
        
    def calcular_autonomia(self):
        return (self._capacidad_tanque * self._consumo_por_litro) - (self.carga * 5)
    