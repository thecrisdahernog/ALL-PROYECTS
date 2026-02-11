import os
os.system('cls')

N1 = float(input("ingrese su primer numero a dividir: "))
N2 = float(input("ingrese su segundo numero a dividir: "))

if N2 == 0:
    print("La division es igual a 0, por lo tanto es un error.")
else:
    print (N1/N2)
# n = float(input("Introduce el dividendo: "))
# m = float(input("Introduce el divisior: "))
# if m == 0:
#     print("¡Error! No se puede dividir por 0.")
# else:
#     print(n/m)