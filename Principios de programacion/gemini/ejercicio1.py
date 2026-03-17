import os
os.system("cls")

print("Bienvenidos al calculador de imc")
print("Ingrese su nombre: ")
nombre = input()
print("Ingrese su peso en kilogramos: ")
peso = float(input())
print("Ingrese su estatura en Metros: ")
estatura = float(input())
imc = peso / (estatura ** 2)
print(f"El imc de {nombre} es: {imc:.2f}")