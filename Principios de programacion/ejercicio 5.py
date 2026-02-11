'''simula el calculo del total de un recibo de compra. define el precio de un producto usando una constante. 
luego, pregunta al usuario cuantas unidades de ese producto desea comprar. 
calcula el subtotal (precio * unidades), el valor del IVA (subtotal * 0.19) y el total final (subtotal + IVA)'''
import os
os.system('cls')


ARROZ = 2500
CARNE = 10000
PLATANOS = 3000
FRIJOLES = 2000

Arroz = float(input("ingrese la cantidad de libras de arroz que desea llevar: "))
Carne = float(input("ingrese la cantidad de libras de carne que desea llevar: "))
Platanos = float(input("ingrese la cantidad de platanos que desea llevar: "))
Frijoles = float(input("ingrese la cantidad de bolsas de frijoles que va a llevar: "))

SubArroz = ARROZ * Arroz
SubCarne = CARNE * Carne
SubPlatano = PLATANOS * Platanos
SubFrijoles = FRIJOLES * Frijoles
Subtotal = SubArroz + SubCarne + SubPlatano + SubFrijoles

IvaTotal = Subtotal * 0.19

TotalFactura = Subtotal + IvaTotal
print(f"esta factura tiene los siguientes valores: \n Arroz = {SubArroz} \n Carne = {SubCarne} \n platanos = {SubPlatano} \n frijoles = {SubFrijoles} \n subtotal = {Subtotal} \n iva = {IvaTotal} \n total factura = {TotalFactura} \n gracias por su compra, vuelva pronto")