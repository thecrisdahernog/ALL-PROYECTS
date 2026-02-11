'''Desarrolle un programa que calcule el area y el perimetro de un rectangulo. debe solicitar al usuario que ingrese el valo9r de la base y la altura del rectangulo'''
import os
os.system('cls')

base = float(input("ingrese por favor la base del rectangulo: "))
altura = float(input("ingrese la altura del rectangulo: "))
area = base * altura
perimetro = (2*base)+(2*altura)
print (f"el area del rectangulo es: {area} \n el perimetro del rectangulo es: {perimetro}")



