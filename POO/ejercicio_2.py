#1. usuario elige piedra, pael o tijera
#2. computadora elige al azar.
#3. se determina el ganador.
#4. se repite hasta que el usuario decide salir

import os
os.system('cls')
import random
Bucle = True

print("Bienvenidos al juego de piedra, papel o tijera")

while Bucle:
    Inicio = int(input(''' 
                        Elije una de las siguientes opciones:
                        1. Jugar
                        2. Salir
                        => '''))
    if Inicio == 1:
        opcion = int(input('''
                            Elije un numero para determinar tu elección:
                            1. Piedra
                            2. Papel
                            3. Tijera
                            => '''))
        if opcion == 1:
            computador = random.randint(1,3)
            if computador == 1:
                print("El computador eligio piedra")
                print("Es un empate")
            elif computador == 2:
                print("El computador eligio Papel")
                print("Perdiste")
            elif computador == 3:
                print("El computador eligio tijeras")
                print("Ganaste")
        elif opcion == 2:
            if computador == 1:
                print("El computador eligio piedra")
                print("Ganaste")
            elif computador == 2:
                print("El computador eligio papel")
                print("Es un empate")
            elif computador == 3:
                print("El computador eligio tijeras")
                print("Perdiste")
        elif opcion == 3:
            if computador == 1:
                print("El computador eligio piedra")
                print("Perdiste")
            elif computador == 2:
                print("El computador eligio papel")
                print("Ganaste")
            elif computador == 3:
                print("El computador eligio tijeras")
                print("Es un empate")
    elif Inicio == 2:
        break
    else:
        print("La opcion elegida no es correcta.")