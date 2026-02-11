import os
os.system('cls')

HorasTrabajo = int(input("ingrese el numero de horas trabajadas en el mes: "))
ValorHora = int(input("ingrese el valor de costo de su hora laboral: "))
resultado = HorasTrabajo * ValorHora
print(f"usted trabajo {HorasTrabajo} Horas y eso le da un total de {resultado} en su quincena")