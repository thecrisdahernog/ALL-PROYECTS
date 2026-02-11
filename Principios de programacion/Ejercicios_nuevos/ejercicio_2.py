import os
os.system('cls')

Revision = "contraseña"
Validacion = input("ingrese por favor la contraseña correcta: ")

if Validacion == Revision:
    print(f"la contraseña ingresada es correcta")
elif Validacion != Revision:
    print(f"la contraseña ingresada es incorrecta")
else:
    print("el valor ingresado es incorrecto")