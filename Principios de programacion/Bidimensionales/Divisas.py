import os
os.system ("cls")

                
Matriz = [
    #USD,#EUR,#MEX,GBP,COP    
    [1,86,1840,76,387194], #USD
    [117,1,], #EUR
    [], #MEX
    [], #GBP
    [] #COP
]

Monedas = ["USD","EUR","MEX","GBP","COP"]

def Menu ():
    try:
        return  int(input("Ingrese una opción\n1. USD\n2. EUR\n3. MEX\n4. GBP\n5. COP\n "))                
    except SyntaxError as ex:
        print (f"Error{ex}")

def Opciones(Op):    
    Op2 = Menu()
    ValorConvertir =  Matriz[Op-1][Op2-1]                 
    ConvertirMoneda(Monedas[Op-1], ValorConvertir,Monedas[Op2-1])

def ConvertirMoneda(MonedaAntes, Taza, MonedaConvertida):
    Monto = float(input(f"Ingrese el monto en {MonedaAntes} que desea convertir: "))
    while Monto < 0:
        print("El monto que digito es invalido")
        Monto = float(input("Ingrese un monto positivo: "))
    Resultado = Monto * Taza
    print(f"Su monto de {Monto} {MonedaAntes} es de {Resultado} {MonedaConvertida}")
    
    
Opcion = Menu()
Opciones(Opcion)