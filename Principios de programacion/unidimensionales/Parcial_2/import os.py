import os
from typing import List, Union

def clear_screen() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

def validate_input(prompt: str, min_val: Union[int, None] = None, max_val: Union[int, None] = None) -> int:
    while True:
        try:
            value = int(input(prompt))
            if (min_val is not None and value < min_val) or (max_val is not None and value > max_val):
                print(f"Error: El valor debe estar entre {min_val} y {max_val}")
                continue
            return value
        except ValueError:
            print("Error: Ingrese un número válido")

def mostrar_menu() -> str:
    return '''
    ===== SISTEMA DE CONTROL DE INVENTARIO =====
    1. Ingresar un artículo al inventario
    2. Visualizar el inventario
    3. Buscar un código en el inventario
    4. Finalizar
    Seleccione una opción: '''

def agregar_articulo(codigos: List[int], nombres: List[str], precios: List[int], stocks: List[int]) -> None:
    # Validar código único
    while True:
        codigo = validate_input("Ingrese el código nuevo (100-1000): ", 100, 1000)
        if codigo in codigos:
            print("Error: El código ya existe")
            continue
        break
    
    # Validar nombre
    while True:
        nombre = input("Ingrese el nombre del artículo: ").strip()
        if not nombre:
            print("Error: El nombre no puede estar vacío")
            continue
        break
    
    precio = validate_input("Ingrese el precio del artículo: ", 0)
    stock = validate_input("Ingrese la cantidad de stock: ", 0)
    
    codigos.append(codigo)
    nombres.append(nombre)
    precios.append(precio)
    stocks.append(stock)
    print("\nArtículo agregado exitosamente!")

def mostrar_inventario(codigos: List[int], nombres: List[str], precios: List[int], stocks: List[int]) -> None:
    if not codigos:
        print("\nEl inventario está vacío")
        return
    
    print("\n{:<10} {:<20} {:<10} {:<10}".format("CÓDIGO", "NOMBRE", "PRECIO", "STOCK"))
    print("-" * 50)
    for i in range(len(codigos)):
        print("{:<10} {:<20} ${:<9} {:<10}".format(codigos[i], nombres[i], precios[i], stocks[i]))

def buscar_articulo(codigos: List[int], nombres: List[str], precios: List[int], stocks: List[int]) -> None:
    codigo = validate_input("\nIngrese el código a buscar: ")
    
    try:
        idx = codigos.index(codigo)
        print("\nArtículo encontrado:")
        print("{:<10} {:<20} {:<10} {:<10}".format("CÓDIGO", "NOMBRE", "PRECIO", "STOCK"))
        print("-" * 50)
        print("{:<10} {:<20} ${:<9} {:<10}".format(codigos[idx], nombres[idx], precios[idx], stocks[idx]))
    except ValueError:
        print("\nEl código no existe en el inventario")

def main():
    codigos = [101, 102, 103, 104]
    nombres = ["De todito", "Chocolate", "Galletas", "Gaseosa"]
    precios = [3000, 2000, 2500, 5000]
    stocks = [5, 4, 6, 4]

    while True:
        clear_screen()
        opcion = validate_input(mostrar_menu(), 1, 4)
        
        if opcion == 1:
            agregar_articulo(codigos, nombres, precios, stocks)
        elif opcion == 2:
            mostrar_inventario(codigos, nombres, precios, stocks)
        elif opcion == 3:
            buscar_articulo(codigos, nombres, precios, stocks)
        else:
            print("\n¡Gracias por usar el sistema!")
            break
            
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()