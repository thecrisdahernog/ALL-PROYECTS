class Vehiculo: 
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def conducir(self):
        print("El vehiculo esta en movimiento")
        
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, color):
        super().__init__(marca, modelo)
        self.color = color
        
    def abrir_puertas(self):
        print("Las puertas estan abiertas")
        
auto1 = Automovil("Toyota", "Car", "Rojo")
print(auto1.marca)
print(auto1.modelo)
print(auto1.color)
auto1.conducir()
auto1.abrir_puertas()  