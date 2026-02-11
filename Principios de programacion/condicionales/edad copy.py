import os
os.system('cls')

edad = int(input("ingrese su edad: "))

if edad >= 18:
    print("mayor de edad")
elif edad >= 0:
    print("menor de edad")
else:
    print("edad invalidad")