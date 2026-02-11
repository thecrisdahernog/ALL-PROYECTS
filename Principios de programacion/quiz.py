import os
import time as tm

os.system('cls')

Nombre = input ("me regala su nombre por favor: ")
print (f"bienvenido {Nombre} a nuetro restaurante")
tm.sleep(5)
Subtotal = float(input("ingrese por favor el subtotal de la cuenta: "))
PropinaPeso = float(input("ingrese el valor de la propina: "))
Propina = Subtotal * (PropinaPeso/100)
print (f"el porcentaje de su propina es: {Propina}")
MontoFinal = Subtotal + Propina
print (f"su cuenta total es: {MontoFinal}")
Personas = float(input("ingrese el numero de personas a dividir en la cuenta: "))
Repartir = MontoFinal / Personas
print (f"el pago total por parte de cada persona es de: {Repartir}")