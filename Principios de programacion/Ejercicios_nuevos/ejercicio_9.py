import os
os.system('cls')

Cantidad = float(input("Cantidad a invertir: "))
Interes = float(input("cantidad en intereses: "))
Años = int(input("Ingrese a cuantos años: "))
Capitalfinal = Cantidad * (1 + Interes / 100) ** Años
print(f"El capital final despues de {Años} años es: {Capitalfinal:.2f}")