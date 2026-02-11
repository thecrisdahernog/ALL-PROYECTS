import os
os.system('cls')
import random

numero_secreto = random.randint(1,25)
adivinado = False

print("Adivina el numero entre 1 y 25")
contador_intentos = 5
while not adivinado and contador_intentos != 0:
    intento = int(input("ingresa tu numero: "))
    if intento < numero_secreto:
        print("El numero es mayor")
    elif intento > numero_secreto:
        print("El numero es menor")
    else:
        print("Felicidades acertaste el numero")
    