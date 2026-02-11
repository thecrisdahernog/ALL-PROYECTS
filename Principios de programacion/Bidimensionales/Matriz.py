import os
os.system('cls')

fila = 2
Cols = 2

Matriz = []

for i in range(fila):
    Arreglo=[]
    for j in range(Cols):
        Valor = int(input("ingrese un numero: "))
        Arreglo.append(Valor)
    
    Matriz.append(Arreglo)

print(Matriz)
