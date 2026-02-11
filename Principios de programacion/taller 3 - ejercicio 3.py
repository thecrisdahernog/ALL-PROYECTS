import os
os.system('cls')

#ingreso de datos
peso = float(input("ingrese su peso en kg: "))
estatura = float(input("ingrese su estatura: "))

#Desarrollo de programa
Imc = peso / (estatura**2)

if Imc >= 30:
    print("tienes Obesidad")
elif Imc >= 25:
    print("tienes sobrepeso")
elif Imc >= 18.5:
    print("tienes peso normal")
elif Imc >= 1:
    print("estas bajo de peso")
else:
    print("peso invalido")