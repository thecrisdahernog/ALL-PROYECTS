#En un campeonato local se registran varios atletas junto con la información de su participación en tres competencias.
#Por cada atleta se deben solicitar los siguientes datos:
#• Nombre completo
#• Disciplina deportiva (por ejemplo: atletismo, natación, ciclismo, etc.)
#• Tiempos obtenidos en las tres competencias realizadas
#El programa debe:
#• Calcular el promedio de tiempos para cada atleta.
#• Mostrar un listado general con el nombre, disciplina y promedio de cada uno.
#• Indicar el atleta con el mejor tiempo promedio general (es decir, el promedio más bajo).
#Nota: Use únicamente arreglos unidimensionales para almacenar los datos. Analice cómo relacionar correctamente la información de cada atleta.

import os
os.system('cls')

Atletas = []
NombreAtleta = []
Diciplinas = []
Tiempos = []
Opciones = 0
Bucle = True
Promedio = 0


while Bucle:
    print("===Bienvenido al calculador de gestion devportiva ===")
    Opciones = int(input('''elija una de las siguientes opciones en el menu: 
                            1. ingresar un deportista
                            2.mostrar informacion general de los deportistas
                            3. salir del programa                            
                            '''))
    if Opciones != 1 and Opciones != 2 and Opciones != 3 and Opciones != 4:
        print("elijio una opcion invalida, por favor vuelva a intentarlo nuevamente")
        Opciones = int(input('''elija una de las siguientes opciones en el menu: 
                            1. ingresar un deportista
                            2.mostrar informacion general de los deportistas
                            3. salir del programa
                            '''))
    if Opciones == 1:
            nombre = input("ingrese por favor el nombre del atleta: ")
            if nombre == "":
                print("ingreso un valor vacio, es un dato invalido en el sistema")
                nombre = input("ingrese por favor el nombre del atleta: ")
            NombreAtleta.append(nombre)
            
            for i in range(1,3+1):
                
                    disc = input(f"ingrese el nombre de la disciplina {i}: ")
                    if disc != "": 
                        Diciplinas.append(disc)
                    tim = float(input(f"ingrese el tiempo de {i} en cada disciplina: "))
                    if tim < 0 and tim == "":
                        print("esta ingresando un valor invalido vuelva a intentarlo")
                    Tiempos.append(tim)                        
            print("los datos del atleta se han ingresado correctamente")
                
    if Opciones == 2:
        for i in range (len(NombreAtleta)):
            print(f'''
{NombreAtleta[i]}

{Diciplinas[i]}
{Tiempos[i]}
{Diciplinas[i+1]}
{Tiempos[i+1]}
{Diciplinas[i+2]}
{Tiempos[i+2]}

                    ''')
            
    if Opciones == 3:
        Bucle = False
            
            
            