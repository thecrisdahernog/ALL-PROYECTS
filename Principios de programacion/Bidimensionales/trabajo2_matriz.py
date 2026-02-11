#crear una matriz de n por n y muestra el valor de X y Y indice
import os
os.system('cls')

Matriz = []
bucle = True

Filas = int(input("ingrese el rango de filas: "))
Cols = int(input("ingrese el rango de Columnas: "))

for i in range(0,Filas+1):
    Arreglo = []
    for j in range(0,Cols+1):
        Valor = i * j
        Arreglo.append(Valor)
    Matriz.append(Arreglo)

print(Matriz)


while bucle:
    ind1 = int(input("ingrese el indice de fila: "))
    ind2 = int(input("ingrese el indice de columna: "))
    if ind1 >= 0 and ind1 < Filas+1 and ind2 >= 0 and ind2 < Cols+1: 
        indice = Matriz[ind1][ind2]
        print(indice)
        indice = int(input("ingrese el nuevo valor para el indice: "))
        Matriz[ind1][ind2] = indice
        print(Matriz)
        bucle = False
    else: 
        print("esta ingresando un valor de indice que no esta en la matriz")
    