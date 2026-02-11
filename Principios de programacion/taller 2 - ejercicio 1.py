import os
os.system('cls')

#entrada de datos
numero = int(input("ingrese por favor un numero al azar, que sera verificado si es par o impar: "))

#desarrollo de programa
if numero % 2 == 0:
    print("este numero es par")
else:
    print("este numero es inpar")