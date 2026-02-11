import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def validate_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("El tiempo debe ser mayor que 0")
                continue
            return value
        except ValueError:
            print("Por favor ingrese un número válido")

def validate_string_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("Este campo no puede estar vacío")

def print_athlete(i, nombres, disciplinas, tiempos1, tiempos2, tiempos3, promedios):
    print("=" * 50)
    print(f"Nombre: {nombres[i]}")
    print(f"Disciplina: {disciplinas[i]}")
    print(f"Tiempo 1: {tiempos1[i]:.2f}")
    print(f"Tiempo 2: {tiempos2[i]:.2f}")
    print(f"Tiempo 3: {tiempos3[i]:.2f}")
    print(f"Promedio: {promedios[i]:.2f}")
    print("=" * 50)

def main():
    nombres = []
    disciplinas = []
    tiempos1 = []
    tiempos2 = []
    tiempos3 = []
    promedios = []

    while True:
        clear_screen()
        print("Bienvenido a DEPOR-APP")
        print("1. Registrar atleta")
        print("2. Ver listado de atletas")
        print("3. Salir")
        
        try:
            opcion = int(input("Seleccione una opción: "))
            
            if opcion == 1:
                nombre = validate_string_input("Ingrese el nombre del atleta: ")
                nombres.append(nombre)
                
                disciplina = validate_string_input("Ingrese la disciplina: ")
                disciplinas.append(disciplina)
                
                tiempo1 = validate_float_input(f"Digite el tiempo de {disciplina} en la primera competencia: ")
                tiempos1.append(tiempo1)
                
                tiempo2 = validate_float_input(f"Digite el tiempo de {disciplina} en la segunda competencia: ")
                tiempos2.append(tiempo2)
                
                tiempo3 = validate_float_input(f"Digite el tiempo de {disciplina} en la tercera competencia: ")
                tiempos3.append(tiempo3)
                
                promedios.append((tiempo1 + tiempo2 + tiempo3) / 3)
                input("\nAtleta registrado. Presione Enter para continuar...")
                
            elif opcion == 2:
                if not nombres:
                    print("\nNo hay atletas registrados")
                    input("Presione Enter para continuar...")
                    continue
                    
                for i in range(len(nombres)):
                    print_athlete(i, nombres, disciplinas, tiempos1, tiempos2, tiempos3, promedios)
                input("\nPresione Enter para continuar...")
                
            elif opcion == 3:
                break
            else:
                print("\nOpción no válida")
                input("Presione Enter para continuar...")
                
        except ValueError:
            print("\nPor favor ingrese un número válido")
            input("Presione Enter para continuar...")

    if nombres:
        print("\n========= Atletas registrados =============")
        for i in range(len(nombres)):
            print_athlete(i, nombres, disciplinas, tiempos1, tiempos2, tiempos3, promedios)

        mejor_indice = promedios.index(min(promedios))
        print("====================== El mejor atleta =====================")
        print_athlete(mejor_indice, nombres, disciplinas, tiempos1, tiempos2, tiempos3, promedios)

if __name__ == "__main__":
    main()