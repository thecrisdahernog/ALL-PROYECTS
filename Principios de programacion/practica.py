# Generador de contraseñas seguras
import string
import secrets
import sys
from random import SystemRandom

rng = SystemRandom()

def pedir_entero(prompt: str, minimo: int = None, maximo: int = None) -> int:
    while True:
        try:
            val = int(input(prompt))
            if minimo is not None and val < minimo:
                print(f"El valor debe ser >= {minimo}.")
                continue
            if maximo is not None and val > maximo:
                print(f"El valor debe ser <= {maximo}.")
                continue
            return val
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")

def nivel_seguridad_por_longitud(long: int) -> tuple:
    # devuelve (nivel_texto, nivel_numérico) para comparaciones
    if long <= 8:
        return ("Bajo", 1)
    if long <= 12:
        return ("Medio", 2)
    if long <= 16:
        return ("Alto", 3)
    return ("Muy alto", 4)

def generar_contrasena(longitud: int) -> str:
    # Asegura al menos una mayúscula, una minúscula y un dígito
    may = secrets.choice(string.ascii_uppercase)
    min_ = secrets.choice(string.ascii_lowercase)
    dig = secrets.choice(string.digits)
    todos = string.ascii_letters + string.digits
    restantes = [secrets.choice(todos) for _ in range(longitud - 3)]
    lista = [may, min_, dig] + restantes
    rng.shuffle(lista)
    return ''.join(lista)

def generar_unicas(cantidad: int, longitud: int, max_intentos_por_item: int = 1000) -> list:
    generadas = []
    vista = set()
    intentos_totales = 0
    while len(generadas) < cantidad:
        if intentos_totales >= cantidad * max_intentos_por_item:
            raise RuntimeError("No se pudieron generar suficientes contraseñas únicas (límite de intentos alcanzado).")
        pwd = generar_contrasena(longitud)
        intentos_totales += 1
        if pwd in vista:
            continue
        vista.add(pwd)
        generadas.append(pwd)
    return generadas

def main():
    print("Generador de contraseñas seguras")
    n = pedir_entero("¿Cuántas contraseñas desea generar? => ", minimo=1)
    longitud = pedir_entero("Longitud deseada para las contraseñas (mín 6, máx 20) => ", minimo=6, maximo=20)

    # comprobar petición razonable (teóricamente siempre posible por el enorme espacio)
    try:
        contrasenas = generar_unicas(n, longitud)
    except RuntimeError as e:
        print("Error:", e)
        sys.exit(1)

    lista_resultados = []
    for pwd in contrasenas:
        nivel_texto, nivel_num = nivel_seguridad_por_longitud(len(pwd))
        lista_resultados.append((pwd, nivel_texto, nivel_num, len(pwd)))

    # mostrar todas
    print("\nContraseñas generadas:")
    for i, (pwd, nivel_texto, _, longitud_pwd) in enumerate(lista_resultados, 1):
        print(f"{i:2d}. {pwd}  | Nivel: {nivel_texto} | Longitud: {longitud_pwd}")

    # determinar la más segura: por nivel numérico, luego por longitud, luego por orden generado
    mejor = max(lista_resultados, key=lambda x: (x[2], x[3]))
    print("\nContraseña más segura generada:")
    print(f"{mejor[0]}  | Nivel: {mejor[1]} | Longitud: {mejor[3]}")

if __name__ == "__main__":
    main()