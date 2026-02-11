'''crea un programa que convierta una cantidad de dias a su equivalente en horas, minutos, y segundos.
el programa debera solicitar al usuario un numero de dias'''

dias = float(input("ingrese el numero de dias a convertir: "))
horas = dias*24
minutos = horas*60
segundos = minutos*60

print(f"los dias ingresados equivalen a {horas} horas, {minutos} minutos y {segundos} segundos")