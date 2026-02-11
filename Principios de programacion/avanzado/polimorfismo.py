class Animal: #perro, gato, vaca
    def hablar(self, sonido):
        print(sonido)
        
#class Perro():
#    def ladrar(self):
#        print("Guau")
class Perro(Animal):
    pass
        
#class Gato():
#    def Maullar(self):
#        print("Miau")
class Gato(Animal):
    pass
        
#class Vaca():
#    def Mu(self):
#        print("Muu")
class Vaca(Animal):
    pass
        
firulais = Perro()
firulais.hablar("Guau")

misifus = Gato()
misifus.hablar("Miau")

Vacalola = Vaca()
Vacalola.hablar("Muu")