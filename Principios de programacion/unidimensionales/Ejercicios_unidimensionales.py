import os
os.system('cls')

MiArreglo = ["Verde","Amarillo","Azul","Morado"]
while True:
    try:
        print("Menú")
        Op = int(input('''Selecciona una opción del menú:
                    1. Agregar:
                    2. Seleccionar:
                    3. Mostrar lista:
                    4. Eliminar:
                    5. Salir:
                    --> 
                    '''))
        
        if Op == 1:
            NewColor = input("Ingrese el nombre del color: ")
            if NewColor != "":
                Existe = False
                for i in MiArreglo:
                    if NewColor.lower() == i.lower():
                        Existe = True
                        break
                if not Existe:
                    MiArreglo.append(NewColor)
                else:
                    print("El color ingresado ya existe en la lista.")  
        elif Op == 2:            
            ColorDeseado = input("Ingrese el nombre del color:  ")
            if ColorDeseado != "":
                Estado = 0
                for i in MiArreglo:
                    if i.upper() == ColorDeseado.upper():
                        print(f"El color solicitado esta en nuestro inventario: {i}")
                        break
                    else:
                        Estado = 1
                if Estado == 1:
                    print("No tenemos disponible ese color.")
        elif Op == 3:
            print(MiArreglo)
            
        elif Op == 4:
            DeleteColor = input("Ingrese el nombre del color a eliminar: ")
            if DeleteColor != "":
                Existe = False
                for i in MiArreglo:
                    if DeleteColor.lower() == i.lower():
                        Existe = True
                        break
                if Existe:
                    MiArreglo.remove(DeleteColor)
                else:
                    print("El color ingresado no existe en la lista.")  
        elif Op == 5:
            break
        else:
            print("Opción invalida.")
    except ValueError as ex:
        print(f"Ha ocurrido una excepción no controlada: {ex}")
        