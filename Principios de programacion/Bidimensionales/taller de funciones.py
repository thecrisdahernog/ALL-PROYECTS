import os
os.system ("cls")

Pacientes = []
Peso = []
estatura = []
Bucle = True

def Menu():
    try:
        return int(input('''
==================================
Bienvenido al calculador de imc
==================================
1. Calcular IMC
2. Mostrar los pacientes registrados
3. Salir
==================================
=> '''))
    except ValueError as ex:
        print(f"Error: {ex}. Por favor ingrese datos válidos.")
        
def IngresoDatos():
    try:
        Nombre = input("Ingrese el nombre del paciente: ")
        PesoPaciente = float(input("Ingrese el peso del paciente en kg: "))
        EstaturaPaciente = float(input("Ingrese la estatura del paciente en metros: "))
        Pacientes.append(Nombre)
        Peso.append(PesoPaciente)
        estatura.append(EstaturaPaciente)
    except ValueError as ex:
        print(f"Error: {ex}. Por favor ingrese datos válidos.")
        
def CalculoIMC(Peso, Estatura):
    Imc = Peso / (Estatura**2)
    return Imc

def MostrarPacientes():
    if len(Pacientes) == 0:
        print("No hay pacientes registrados")
    else:
        for i in range(len(Pacientes)):
            Imc = CalculoIMC(Peso[i], estatura[i])
            print("==================================")
            print(f"Paciente: {Pacientes[i]}")
            print(f"Peso: {Peso[i]} kg")
            print(f"Estatura: {estatura[i]} m")
            print(f"IMC: {Imc:.2f}")
            if Imc >= 30:
                print("Estado: Obesidad")
            elif Imc >= 25:
                print("Estado: Sobrepeso")
            elif Imc >= 18.5:
                print("Estado: Peso normal")
            else:
                print("Estado: Bajo peso")
            print("==================================")

while Bucle:
    Opcion = Menu()
    if Opcion == 1:
        IngresoDatos()
    elif Opcion == 2:
        MostrarPacientes()
    elif Opcion == 3:
        print("gracias por usar el programa, vuelva pronto...")
        Bucle = False
    else:
        print("Opción inválida, por favor intente nuevamente.")