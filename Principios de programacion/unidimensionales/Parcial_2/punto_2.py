import os
os.system('cls')

Codigos = [101,102,103,104]
Nombres = ["De todito","Chocolate","Galletas","gaseosa"]
Precios = [3000,2000,2500,5000]
Stocks = [5,4,6,4]
Opciones = 0
Bucle = True


while Bucle:
    print("===== Bienvenido al programa de control de inventario")
    Opciones = int(input('''Elija una de las siguientes opciones
                            1. ingresar un articulo al inventario
                            2. visualizar el inventario
                            3. buscar un codigo en el inventario
                            4. finalizar
                            '''))
    if Opciones != 1 and Opciones != 2 and Opciones != 3 and Opciones != 4:
        print("ingreso un valor invalido, intente nuevamente")
        Opciones = int(input('''Elija una de las siguientes opciones
                            1. ingresar un articulo al inventario
                            2. visualizar el inventario
                            3. buscar un codigo en el inventario
                            4. finalizar
                            '''))
    if Opciones == 1:
        codigo = int(input("Ingrese el codigo nuevo a crear entre 100 y 1000: "))
        if codigo < 100 or codigo > 1000:
            print("El valor ingresado es invalido, intente nuevamente")
            codigo = int(input("Ingrese el codigo nuevo a crear entre 100 y 1000: "))
        Codigos.append(codigo)
        
        NombreArticulo = input("Ingrese el nombre del nuevo articulo: ")
        if NombreArticulo == "":
            print("esta ingresando un dato invalido, intente nuevamente")
            NombreArticulo = input("Ingrese el nombre del nuevo articulo: ")
        Nombres.append(NombreArticulo)
        
        precio = int(input("ingrese el precio del nuevo articulo: "))
        if precio == "" or precio < 0:
            print("el valor agregado es invalido, intente nuevamente")
            precio = int(input("ingrese el precio del nuevo articulo: "))
        Precios.append(precio)
        
        stock = int(input("ingrese la cantidad de stock: "))
        if stock == "" or stock < 0:
            print("la cantidad de stock ingresada es invalida, intente nuevamente")
            stock = int(input("ingrese la cantidad de stock: "))
        Stocks.append(stock)
        
    if Opciones == 2:
        print(f"CODIGO NOMBRE PRECIO STOCK")
        for i in range(len(Codigos)):
            print(f"{Codigos[i]} {Nombres[i]} {Precios[i]} {Stocks[i]}")
    if Opciones == 3:
        Encontrado = False
        Busqueda = int(input("ingresar el codigo a buscar"))
        for i in range(len(Codigos)):
            if Busqueda == Codigos[i]:
                print(f"{Codigos[i]} {Nombres[i]} {Precios[i]} {Stocks[i]}")
                Encontrado = True
        if Encontrado == False:
            print("el codigo ingresado no ha sido encontrado")
    if Opciones == 4:
        Bucle = False
        
            