#class Cuenta:
#    def __init__(self,saldo):
#        self.saldo = saldo
#        
#cuenta1= Cuenta(1000000)
#cuenta1.saldo = -5000
#print(cuenta1.saldo)

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self._precio = precio
        
    def cambiar_precio(self, nuevo_precio):
        if nuevo_precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        else   :
            self._precio = nuevo_precio
            
    def mostrar_precio(self):
        print(self._precio)

p = Producto("Borojopower", 10000)

try:
    #codigo que puede fallar
    p.cambiar_precio(-8000)
except ValueError as e: 
    #que hacer si falla
    print("Error",e)
    
finally:
    p.mostrar_precio()





