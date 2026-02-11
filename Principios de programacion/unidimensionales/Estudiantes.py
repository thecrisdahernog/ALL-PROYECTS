#vamos a crear un codigo que capture a 3 estudiantes y y a cada uno le capture 3 notas
# y que muestre al final las 3 notas de cada uno

import os
os.system('cls')

#Declaracion de variables
Estudiantes = []
Nota1 = []
Nota2 = []
Nota3 = []

#inicio 
for es in range(1,4):
    Estudiante = input(f"Ingrese el nombre del estudiante {es} ")
    Estudiantes.append(Estudiante)
    for n in range(1,4):
        Nota = float(input(f"ingrese la nota {n}: "))
        if es == 1:
            Nota1.append(Nota)
        elif es == 2:
            Nota2.append(Nota)
        elif es == 3:
            Nota3.append(Nota)
n = 0            
for i in Estudiantes:
    n+=1
    if n == 1:
        print(f"Las notas para el estudiante {i} son: {Nota1}")
    if n == 2:
        print(f"Las notas para el estudiante {i} son {Nota2}")
    if n == 3:
        print(f"Las notas para el estudiante {i} son {Nota3}")        

