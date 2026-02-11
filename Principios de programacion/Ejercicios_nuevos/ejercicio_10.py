import os
os.system('cls')

PAYASOS = 112
MUÑECAS = 75


Payaso = int(input("Ingrese la cantidad de payasos a vender: "))
while Payaso < 0 :
    Payaso = int(input("Ingrese un valor correcto de payasos a vender: "))
    break
Muñeca = int(input("ingrese la cantidad de muñecas a vender: "))
while Muñeca < 0:
    Muñeca = int(input("ingrese un valor correcto de muñecas a vender: "))
    break
PesoPayaso = Payaso * PAYASOS
PesoMuñeca = Muñeca * MUÑECAS
PesoPaquete = PesoPayaso + PesoMuñeca
print(f"El numero total de payasos es {Payaso} y el numero total de muñecas es {Muñeca}\n el paso total del paquete es de {PesoPaquete} Kg")