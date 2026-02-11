import os
os.system('cls')

#ingreso de datos
edad = int(input("ingrese su edad: "))

#desarrollo de programa
if edad >0:
    if edad >= 18:
        print ("Acceso permitido: BIEN PUEDA")
    else:
        print("Acceso denegado: LARGUESE")
else:
    print("la edad ingresada es invalida")