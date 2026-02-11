class Miclase:
    def __init__(self):
        self.publico = 24
        self._privada = "soy privado"
        
    def publico(self):
        print("Soy publico")
        
    def _privado(self):
        print("Soy privado")
        
class Persona():
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
        
    def get_nombre(self):
        return self._nombre
    
    def set_nombre(self, nombre):
        self._nombre = nombre

juan = Persona("juan", 40)
print(juan.get_nombre())