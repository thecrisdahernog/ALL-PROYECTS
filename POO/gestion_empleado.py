import os
os.system('cls')

class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario
        
    def mostrar_informacion(self):
        print("empleado: ", self.nombre)
        print("Cargo: ", self.cargo)
        print("Salario: ", self.salario)
        print("-----------------------")
        
    def aumentar_salario(self, porcentaje):
        aumento = self.salario * (porcentaje / 100)
        self.salario = self.salario + aumento
        print("El saladior de" , self.nombre, "Ha sido actualizado.")
        print("Nuevo salario: ", self.salario)
        
    def cambiar_Cargo(self, nuevo_cargo):
        self.cargo = nuevo_cargo
        print(self.nombre, "ahora trabaja como ", self.cargo)
        
empleado1 = Empleado("Oscar Cantillo", "Morranero", 50000000)
empleado2 = Empleado("Ivan Rebolledo", "Asistente de Morraneria", 25000000)

empleado1.mostrar_informacion()
empleado2.mostrar_informacion()

empleado1.cambiar_Cargo("Morranero Senior")
empleado2.cambiar_Cargo("Morranero Niverl Mid")

empleado2.aumentar_salario(5)

print("Informe de empleados actualizado")
empleado1.mostrar_informacion()
empleado2.mostrar_informacion()
