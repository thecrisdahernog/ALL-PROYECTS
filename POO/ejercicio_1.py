#Ejercicio 1: 
#1. el programa genera un numero secreto entre 1 y 25
#2. el usuario intenta adivinarlo (5 intentos)
#3. me dan pistas: mayor y menor
#4. Mensaje final: Victoria o derrota

import os
os.system('cls')
import random

vidas = 5
numero_secreto = random.randint(1, 25)
print("Bienvenido al juego de adivinar el numero secreto")  
print("Tienes 5 intentos para adivinar el numero secreto entre 1 y 25")

while vidas > 0:
    numero_usuario = int(input("Ingrese un numero: "))
    if numero_usuario == numero_secreto:
        print("Felicidades, has adivinado el numero secreto")
        break
    elif numero_usuario < numero_secreto:
        print("El numero secreto es mayor")
    else:
        print("El numero secreto es menor")
    vidas -= 1
    print(f"Te quedan {vidas} vidas")
else:
    print(f"Has perdido. El numero secreto era {numero_secreto}")