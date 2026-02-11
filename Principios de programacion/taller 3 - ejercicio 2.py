import os
os.system('cls')

#entrada de datos
nota = float(input("ingrese su Nota por favor: "))

#desarrollo de programa
if nota > 100:
    print("su nota es invalida")
elif nota >= 90:
    print("su nota es: EXCELENTE")
elif nota >= 70:
    print("su nota es: BUENO")
elif nota >= 50:
    print("su nota es: SUFICIENTE")
elif nota >= 0:
    print("su nota es: REPROBADO")
else:
    print("nota invalida")