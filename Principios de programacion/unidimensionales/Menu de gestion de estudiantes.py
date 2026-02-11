#Menú de Gestión de Estudiantes
#Diseñe un programa que presente un menú de opciones con las siguientes funcionalidades:
#Agregar estudiantes: registrar por cada estudiante su nombre completo y un conjunto de notas.
#Ver listado de estudiantes: mostrar en pantalla todos los estudiantes registrados junto con sus datos completos y el promedio de las notas ingresadas.
#Terminar el programa: finalizar la ejecución del sistema.
#El programa debe permitir que el usuario seleccione una opción y se ejecute la acción correspondiente, manteniéndose en ejecución hasta que se elija la opción de salida.

import os
os.system("cls")

#Declaracion de variables
Estudiantes = []
Nota1 = []
Nota2 = []
Nota3 = []
Bucle = True
Opciones = 0

#Iniciamos el ciclo - menu
while Bucle:
    Opciones = int(input("bienvenidos al programa\n1. para registrar estudiates\n2. para ver listado de estudiantes\n3. Para cerrar el programa"))
    
    #Validacion que las opciones sean correctas
    while Opciones != 1 and Opciones != 2 and Opciones != 3:
        print("ingrese un valor valido")
        Opciones = int(input("bienvenidos al programa\n1. para registrar estudiates\n2. para ver listado de estudiantes\n3. Para cerrar el programa: \n"))
    
    #opcion 1 - registrar estudiantes    
    if Opciones == 1:
        Estu = input("ingrese su nombre: ")
    
        #Validamos que ingrese su nombre    
        while Estu == "":
            estu = input("Digite un Nombre valido: ")
        Estudiantes.append(Estu)
        
        #Capturamos nota 1
        n1 = float(input("digite la nota 1: "))
        
        #Validamos nota 1
        while n1 <0 or n1 >5:
            n1 = float(input("digite una nota validad teniendo en cuenta el rango de 0 - 5: "))
        
        #Almacenamos nota 1 en nuestro arreglo
        Nota1.append(n1)
        #Capturamos nota 2
        n2 = float(input("Digite la nota 2: "))
        #Validamos nota 2
        while n2 <0 or n2 >5:
            n2 = float(input("digite una nota validad teniendo en cuenta el rango de 0 - 5: "))
        #Capturamos nota 2    
        Nota2.append(n2)
        
        #Capturamos nota 3
        n3 = float(input("Digite la nota 3: "))
        #Validamos nota 3
        while n3 <0 or n3 >5:
            n3 = float(input("digite una nota validad teniendo en cuenta el rango de 0 - 5: "))
        #Capturamos nota 3    
        Nota3.append(n3)
    #opcion 2 - Mostrar listado de estudiantes    
    elif Opciones == 2:
        #Validamos opcion de listado de estudiantes
        if len(Estudiantes) == 0:
            print("no hay estudiantes registrados")
        #Mostramos listado de estudiantes
        else:     
            for i in range(len(Estudiantes)):
                print("=========================//=================")
                print(f"Estudiantes en la posicion {i}: {Estudiantes[i]}")
                print(f"Nota1: {Nota1[i]}")
                print(f"Nota2: {Nota2[i]}")
                print(f"Nota3: {Nota3[i]}")
                print(f"Definitiva: {(Nota1[i] + Nota2[i] + Nota3[i])/3}")
                print("=========================//=================")
    #opcion 3 - Cerrar el programa
    else:
        Bucle = False
        print("Hasta luego, vuelva pronto")
        

    

    

        