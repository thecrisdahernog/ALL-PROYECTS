import os
os.system('cls')

Nombres = []
FrecuenciasC = []
Temperaturas = []
FrecuenciasR = []
#Cardio = ()
#Temp = ()
#Resp = ()
Bucle = True

def Menu():
    try:
        return int(input('''
======================================
Bienvenido al calculador de imc
======================================
1. registrar un paciente
2. Mostrar los pacientes registrados
3. Salir
======================================
=> '''))
    except ValueError as ex:
        print(f"Error: {ex}. Por favor ingrese datos válidos.")
        
def IngresoPacientes():
    try: 
        Nombre = input("ingrese el nombre del paciente: ")
        if Nombre != "" and Nombre != " ":
            Nombres.append(Nombre)
            Cardio = int(input("ingrese la frecuencia cardiaca del paciente (rango: 30 - 200 Lpm): "))
            if Cardio > 30 and Cardio < 200: 
                FrecuenciasC.append(Cardio)
                temp = float(input("ingrese la temperatura en Celsius del paciente (rango: 30°c - 42°C): "))
                if temp > 30 and temp < 42:
                    Temperaturas.append(temp)
                    Resp = int(input("ingrese la frecuencia respiratoria del paciente (rango: 5 - 50 rpm): "))
                    if Resp > 5 and Resp < 50:
                        FrecuenciasR.append(Resp)
                        print("los datos fueron registrados correctamente")
    except ValueError as Ex:
        print(f"Error: {Ex}. Por favor ingrese datos validos. ")

def MostrarPacientes():
    if len(Nombres) == 0:
        print("No hay pacientes registrados. ")
    else: 
        for i in range(len(Nombres)):
            print("======================================")
            print(f"Paciente: {Nombres[i]}")
            print(f"el ritmo cardiaco es: {FrecuenciasC[i]} lpm")
            if FrecuenciasC[i] > 100 or FrecuenciasC[i] < 60:
                print("el ritmo Cardiaco del paciente se encuentra fuera del Rango normal.")
                print("Por favor hacer seguimiento.")
            else:
                print("el ritmo cardiaco del paciente se encuentra estable")                
            print(f"la temperatura es de: {Temperaturas[i]} C°")
            if Temperaturas[i] > 37.2 or Temperaturas[i] < 36.1:
                print("La temperatura del paciente se encuentra fuera del rango normal")
                print("Por favor hacer seguimiento")
            else:
                print("La temperatura del paciente se encuentra estable")
            print(f"La frecuencia respiratoria es de: {FrecuenciasR[i]} rpm")
            if FrecuenciasR[i] > 20 or FrecuenciasR [i] < 12:
                print("La frecuencia respiratoria del paciente se encuentra fuera del rango normal")
                print("por favor hacer seguimiento")
            else:
                print("LA frecuencia respiratoria del paciente se encueentra estable")
            print("======================================")

def EstadoDelPaciente(FrecuenciasC,Temperaturas,FrecuenciasR):
    if FrecuenciasC < 60 or FrecuenciasC > 100:
        if Temperaturas < 36.1 or Temperaturas > 37.2:
            if FrecuenciasR < 12 or FrecuenciasR > 20:
                print("El Estado de salud del paciente es riesgoso, debe tener atencion.")
            else:
                print("El estado de salud del paciente no esta en riesgo.")
                
def RangosSignosVitales(FrecuenciasC,Temperaturas,FrecuenciasR):
    if FrecuenciasC < 60:        
        print("el ritmo Cardiaco del paciente se encuentra fuera del Rango normal.")
        print("Por favor hacer seguimiento.")
    elif FrecuenciasC > 100:
        print("el ritmo Cardiaco del paciente se encuentra fuera del Rango normal.")
        print("Por favor hacer seguimiento.")
    else:
        print("el ritmo cardiaco del paciente se encuentra estable")
        print("Dentro de los rangos normales.")
        
    if Temperaturas < 36.1:        
        print("el ritmo Cardiaco del paciente se encuentra fuera del Rango normal.")
        print("Por favor hacer seguimiento.")
    elif Temperaturas > 37.2:
        print("el ritmo Cardiaco del paciente se encuentra fuera del Rango normal.")
        print("Por favor hacer seguimiento.")
    else:
        print("el ritmo cardiaco del paciente se encuentra estable")
        print("Dentro de los rangos normales.")
        
    if FrecuenciasR < 12:        
        print("el ritmo Cardiaco del paciente se encuentra fuera del Rango normal.")
        print("Por favor hacer seguimiento.")
    elif FrecuenciasR > 20:
        print("el ritmo Cardiaco del paciente se encuentra fuera del Rango normal.")
        print("Por favor hacer seguimiento.")
    else:
        print("el ritmo cardiaco del paciente se encuentra estable")
        print("Dentro de los rangos normales.")
                
while Bucle:
    Opcion = Menu()
    if Opcion == 1:
        IngresoPacientes()
    elif Opcion == 2:
        MostrarPacientes()
        #EstadoDelPaciente()
        #RangosSignosVitales()
    elif Opcion == 3:
        print("gracias por usar el programa, vuelva pronto...")
        Bucle = False
    else:
        print("Opción inválida, por favor intente nuevamente.")