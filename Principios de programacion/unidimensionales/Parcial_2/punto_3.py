import os
os.system('cls')

periodos = 0
Letra = "*"
Bucle = True

while Bucle:  
    try:
        while Bucle:
            periodos = int(input("ingrese el numero de periodos: "))
            Letra = "*"
            if periodos < 0:
                print("ingreso un numero invalido, intente nuevamente: ")
                periodos = int(input("ingrese el numero de periodos: "))
                Bucle = False
                
            for i in range(1,periodos+1):
                print(Letra*i)
                
            Bucle = False
    except ValueError as Ex:
        print("Valor erroneo ingresado")