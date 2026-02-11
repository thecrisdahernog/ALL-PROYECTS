import os
os.system('cls')

Num1 = 0
Num2 = 0 

def Buscarpar():
    for i in range(Num1,Num2):
        if i % 2 == 0:
            print(f"el numero {i} es par")
        else:
            print(f"el numero {i} es impar")
try:
    Num1 = int(input("ingrese un numero positivo inicial: "))
    Num2 = int(input("ingrese un numero positivo final: "))
    Buscarpar()
except ValueError as Ex:
    print("Valor erroneo ingresado, intente nuevamente")