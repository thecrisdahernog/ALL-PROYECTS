import os
os.system('cls')

Nombres = []
Disciplinas = []
Tiempo1 = []
Tiempo2 = []
Tiempo3 = []
Promedios = []
Bucle = True

while Bucle:
    opcion = int(input("Bienvenido a DEPOR-APP ingrese \n1. Para registrar atleta.\n 2.para ver el listado de atletas.\n 3. para salir"))
    #validamos la opcion ingresada
    if opcion == 1:
        Nombre = input("ingrese un nombre\n")
        #valido el dato capturado
        Nombres.append(Nombre)
        
        Disciplina = input("ingrese la disciplina\n")
        #valido el dato capturado
        Disciplinas.append(Disciplina)
        
        tiempo1 = float(input(f"Digite el tiempo de la disciplina {Disciplina} durante la primera competencia\n"))
        #Validacion del tiempo optenido
        Tiempo1.append(tiempo1)
        
        tiempo2 = float(input(f"Digite el tiempo de la disciplina {Disciplina} durante la primera competencia\n"))
        #Validacion del tiempo optenido
        Tiempo2.append(tiempo2)
        
        tiempo3 = float(input(f"Digite el tiempo de la disciplina {Disciplina} durante la primera competencia\n"))
        #Validacion del tiempo optenido
        Tiempo3.append(tiempo3)
        
        
        Promedios.append((tiempo1+tiempo2+tiempo3)/3)
    elif opcion == 2:
        for i in range(len(Nombres)):
            print("================================================")
            print(f"nombre: {Nombres[i]}")
            print(f"Disciplina: {Disciplinas[i]}")
            print(f"Tiempo 1: {Tiempo1[i]}")
            print(f"Tiempo 2: {Tiempo2[i]}")
            print(f"Tiempo 3: {Tiempo3[i]}")
            print(f"Promedio: {Promedios[i]}")
            print("================================================")
    else:
        print("Hasta luego...")
        Bucle = False
        
print("========= Atletas registrados =============")
for i in range(len(Nombres)):
            print("================================================")
            print(f"nombre: {Nombres[i]}")
            print(f"Disciplina: {Disciplinas[i]}")
            print(f"Tiempo 1: {Tiempo1[i]}")
            print(f"Tiempo 2: {Tiempo2[i]}")
            print(f"Tiempo 3: {Tiempo3[i]}")
            print(f"Promedio: {Promedios[i]}")
            print("================================================")
            
print("====================== el mejor atleta =====================")
print(f"Nombre: {Nombres[Promedios.index(min(Promedios))]}")
print(f"Disciplina: {Disciplinas[Promedios.index(min(Promedios))]}")
print(f"tiempo 1:{Tiempo1[Promedios.index(min(Promedios))]}")
print(f"tiempo 2:{Tiempo2[Promedios.index(min(Promedios))]}")
print(f"tiempo 3:{Tiempo1[Promedios.index(min(Promedios))]}")
print(f"Promedio: {min(Promedios)}")