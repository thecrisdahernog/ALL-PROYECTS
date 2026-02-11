import os
os.system('cls')

Dinero = 0


Dinero = float(input("Ingrese la cantidad de dinero que va a ingresar a la cuenta: "))
Intereses = Dinero * 0.04
Año1 = Intereses + Dinero
Año2 = Año1 * 2
Año3 = Año1 * 3
print(f"El dinero en la cuenta despues del primer año es: {Año1:.2f}\n El dinero en la cuenta despues del segundo año es: {Año2:.2f}\n El dinero en la cuenta despues del tercer año es: {Año3:.2f}")
print(f"El dinero del primer año es: {Año1:.2f}")
print(f"el dinero del segundo año es: {Año2:.2f}")
print(f"el dinero del tercer año es: {Año3:.2f}")