import os
os.system('cls')
bucle = True


while bucle:
    try:
        Numero = int(input("ingrese un numero positivo: "))
        if Numero > 0:
            suma = (Numero * (Numero+1))/2
            print("La suma de los numeros desde 1 hasta", Numero, "es:", suma)
        else:
            print("El numero ingresado no es valido")
        bucle = False
    except ValueError as Ex:
        print("Valor erroneo ingresado, intente nuevamente")