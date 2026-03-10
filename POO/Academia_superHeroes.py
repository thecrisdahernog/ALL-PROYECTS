class SuperHeroe:
    def __init__(self, nombre, energia, poder_base):
        if energia < 0:
            raise ValueError("La energía no puede ser negativa.")
        elif poder_base < 0:
            raise ValueError("El poder base no puede ser negativo.")
        else: 
            self.nombre = nombre
            self._energia = energia
            self._poder_base = poder_base
            
    def mostrar_estado(self):
        print(f"SuperHeroe: {self.nombre}, Energia: {self._energia}")
            
    def recibir_Daño(self, daño):
        if daño < 0:
            raise ValueError("El daño no puede ser negativo.")
        else:
            self._energia -= daño
            if self._energia < 0:
                self._energia = 0    

    def usar_poder(self, enemigo):
        print(f"{self.nombre} ha atacado a su enemigo {enemigo.nombre} ")
        enemigo.recibir_Daño(self._poder_base)
            
class SuperFuerza(SuperHeroe):
    def __init__(self, nombre, energia, poder_base, fuerza):
        super().__init__(nombre, energia, poder_base)
        self._fuerza = fuerza
        
    def poder_especial(self, enemigo):
        print(f"{self.nombre} ha usado su poder especial de SuperFuerza contra {enemigo.nombre}")
        enemigo.recibir_Daño(self._poder_base + self._fuerza)
        
class SuperVelocidad(SuperHeroe):
    def __init__(self, nombre, energia, poder_base, velocidad):
        super().__init__(nombre, energia, poder_base)
        self._velocidad = velocidad
        
    def poder_especial(self, enemigo):
        print(f"{self.nombre} ha usado su poder especial de SuperVelocidad contra {enemigo.nombre}")
        enemigo.recibir_Daño(self._poder_base + self._velocidad *2)
        
try:
    heroe1 = SuperFuerza("Hulk", 100, 20, 30)
    heroe2 = SuperVelocidad("Flash", 80, 15, 25)
    
    heroe1.mostrar_estado()
    heroe2.mostrar_estado()
    
    heroe1.usar_poder(heroe2)
    heroe2.mostrar_estado()
    
    heroe2.poder_especial(heroe1)
    heroe1.mostrar_estado()
except ValueError as e:
    print(e)