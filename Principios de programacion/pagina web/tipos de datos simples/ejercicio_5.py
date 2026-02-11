import os
os.system('cls')
Bucle = True
while Bucle:    
    try:
        HoraTrabajo = int(input("Ingrese la cantidad de horas trabajadas: "))    
        ValorHora = float(input("Ingrese el valor por hora trabajada: "))   
        SalarioBruto = HoraTrabajo * ValorHora   
        
        print(f"El salario bruto es de: {SalarioBruto}")
    except ValueError as Ex:     
        print("Valor erroneo ingresado, intente nuevamente")
    Bucle = False