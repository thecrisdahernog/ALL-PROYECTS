import os
os.system('cls')

edad = int(input("ingrese su edad: "))

if edad >0:
    if edad >= 21:
        print ("usted es mayor de edad")
    else:
        print("usted es menor de edad")
else:
    print("la edad ingresada es invalida")