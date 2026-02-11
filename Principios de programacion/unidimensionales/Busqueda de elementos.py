#Busqueda de elementos
#se tiene una lista de numeros enteros ingresados por el usuario
#1. Guarde todos los numeros en un arreglo
#2. Solicite un numero a buscar
#3. Muestre en que posiciones aparece ese numero y cuantas veces se repite

import os
os.system('cls')

#Declaracion de variables
Numeros = []
Bucle = True
Opciones = 0

#inicio dde programa
while Bucle:
    Opciones = int(input('''Bienvenido al programa para numeros
                            elija por favor una opcion del siguiente listado
                            1. ingresar un numero nuevo
                            2. buscar un numero para mostrar en que posicion aparece y cuantas veces se repite
                            3. Finalizar programa
                            '''))
    
    #validacion de opciones correctas
    while Opciones != 1 and Opciones != 2 and Opciones != 3:
        print("ingrese por favor un valor valido")
        Opciones = int(input('''Bienvenido al programa para numeros
                            elija por favor una opcion del siguiente listado
                            1. ingresar un numero nuevo
                            2. buscar un numero para mostrar en que posicion aparece y cuantas veces se repite
                            3. Finalizar programa
                            '''))
    
    #Opcion 1 - Ingreso de numeros al listado
    if Opciones == 1:
        NumNew = int(input("ingrese el numero nuevo a ingresar"))
        Numeros.append(NumNew)
    #Opcion 2 - Buscando en el listado de numeros    
    elif Opciones == 2:
        Buscar = int(input("ingrese por favor el numero que va a buscar: "))
        for i in range(len(Numeros)):
            if Numeros[i] == Buscar:
                print(f"el numero {Buscar} esta en la posicion {i+1}")              
        print(f"se repite {Numeros.count(Buscar)} veces.")
    #opcion 3 - Finalizando programa    
    else: 
        Bucle = False
        print("Ha finalizado el programa, vuelva pronto")

            
    