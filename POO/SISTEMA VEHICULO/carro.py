from vehiculo import Vehiculo

class Carro(Vehiculo):
    def __init__(self, marca, capacidad_tanque, consumo_por_litro):
        super().__init__(marca, capacidad_tanque)
        self._consumo_por_litro = consumo_por_litro
        
    def calcular_autonomia(self):
        return self._capacidad_tanque * self._consumo_por_litro