import os
os.system('cls')

#entrada de datos
edad = int(input("ingrese su edad por favor: "))

#desarrollo de programa
if edad >= 65:
    print("eres un Adulto Mayor")
elif edad >= 18:
    print("eres un Adulto")
elif edad >= 12:
    print("eres un Adolescente")
elif edad >= 1:
    print("eres un niño")
else:
    print("edad invalida")