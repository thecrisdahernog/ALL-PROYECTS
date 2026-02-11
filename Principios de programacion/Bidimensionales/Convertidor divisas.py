import os
os.system('cls')

MonedaActual = 0
MonedaConvertir = 0
Ingreso = 0
Bucle = True

Matriz = [    
    [1,0.86,18.43,3880,0.76],
    [1.16,1,21.46,4536,0.88],
    [0.047,0.054,1,211.27,0.041],
    [0.00026,0.00022,0.0047,1,0.00019],
    [1.31,1.44,3042,1.00,1]     
]
Monedas = ["USD","EUR","MEX","COP","GBP"]

def Menu():
    try:
        return int(input('''
            |===========================|
            |   CONVERTIDOR DE DIVISAS  |
            |===========================|
            | 1. USD                    |
            | 2. EUR                    |
            | 3. MEX                    |
            | 4. COP                    |
            | 5. GBP                    |
            |===========================|
            => Seleccione una moneda: '''))
    except SyntaxError as Ex:
        print("Valor erroneo ingresado, intente nuevamente")
                    
def opciones(Op):        
    Op2 = Menu()
    ValorConvertir = Matriz[Op-1][Op2-1]                 
    ConvertirMoneda(Monedas[Op-1], ValorConvertir,Monedas[Op2-1])
                
def ConvertirMoneda(MonedaAntes, Taza, MonedaConvertida):
    Monto = float(input(f"Ingrese el monto en {MonedaAntes} que desea convertir: "))
    while Monto < 0:
        print("El monto que digito es invalido")
        Monto = float(input("Ingrese un monto positivo: "))
    Resultado = Monto * Taza
    print(f"Su monto de {Monto} {MonedaAntes} es de {Resultado} {MonedaConvertida}")
    
def Listartasas():
    for i in range(len(Monedas)):        
            print(f'''-----------------------------------
{Monedas[i]} a {Monedas[0]} es de {Matriz[i][0]}
{Monedas[i]} a {Monedas[1]} es de {Matriz[i][1]}
{Monedas[i]} a {Monedas[2]} es de {Matriz[i][2]}
{Monedas[i]} a {Monedas[3]} es de {Matriz[i][3]}
{Monedas[i]} a {Monedas[4]} es de {Matriz[i][4]}''')
                    
while Bucle:
    while Bucle:
        Ingreso = int(input('''
    Bienvenido al programa de conversion de divisas
    ============================================
    1. Convertir divisas
    2. listar tasas de cambio
    3. Salir
    ============================================
    => '''))
        break
    while Ingreso != 1 and Ingreso != 2 and Ingreso != 3:
        print("Ingrese una opcion valida")
        Ingreso = int(input('''
    Bienvenido al programa de conversion de divisas
    ============================================
    1. Convertir divisas
    2. listar tasas de cambio
    3. Salir
    ============================================
    => '''))
            
    if Ingreso == 1:
        print("Convertir divisas")
        Opcion = Menu()
        opciones(Opcion)    
    
    if Ingreso == 2:
        print("Las tasas de cambio disponibles son:")
        Listartasas()                
            
    if Ingreso == 3:
        print("Gracias por usar el programa")
        Bucle = False            
        
                    
        




# Indice = Matriz[MonedaActual][MonedaConvertir]
# Monto = float(input("Ingrese el monto a convertir: "))
# Conversion = Monto * Indice
# print(f'El monto convertido es: {Conversion}')

