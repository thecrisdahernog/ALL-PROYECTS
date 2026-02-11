import os
os.system('cls')

#Declaracion de variables
NumEstudiantes = []
Calificaciones = []
Opciones = []
NotaAlta = 0
NotaBaja = 0
Aprobados = 0
Desaprobados = 0
Promedio = 0
Bucle = True

while Bucle:
    print("Bienvenidos al programa de evaluacion del curso")
    NumEstudiantes = int(input("ingrese el numero de estudiantes que tiene en el curso: "))
    if NumEstudiantes <= 0:
        print("esta ingresando un valor no permitido, por favor vuelva a intentarlo")
        NumEstudiantes = int(input("ingrese el numero de estudiantes que tiene en el curso: "))

    for i in range(1,NumEstudiantes+1):
        Notafinal = float(input(f"ingrese la nota final de cada estudiante {i}: "))
        if Notafinal > 5 or Notafinal < 0:
            print("ingreso una nota invalida, ingrese nuevamente la nota por favor")
            Notafinal = float(input(f"ingrese la nota final de cada estudiante {i}: "))
        Calificaciones.append(Notafinal)
        
        
    for i in range(0,NumEstudiantes):
        
        if Calificaciones[i] >= Calificaciones[NotaAlta]:
            NotaAlta = i
        if Calificaciones[i] <= Calificaciones[NotaBaja]:
            NotaBaja = i
        if Calificaciones[i] >= 3:
            Aprobados += 1
        if Calificaciones[i] < 3:
            Desaprobados += 1
        Promedio += Calificaciones[i]
    Promedio = Promedio / NumEstudiantes
        
    Bucle = False
    
print(f'''
        El total de estudiantes ingresados fue: {NumEstudiantes}
        El promedio de las notas de los estudiantes es: {Promedio}
        la nota mas alta es: {Calificaciones[NotaAlta]}
        La nota mas Baja es: {Calificaciones[NotaBaja]}
        El total de estudiantes aprobados es: {Aprobados}
        El total de estudiantes desaprobados es: {Desaprobados}
            ''')    
    
    