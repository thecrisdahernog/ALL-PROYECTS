#Control de temperaturas
#Un sistema meterologico necesita almacenar las temperaturas registradas en una semana
#1. guarde las 7 temperaturas en un arreglo
#2. Muestre las temperaturas promedio
#3. Indique en que dia se presento la temperatura mas alta y la mas baja

import os
os.system('cls')

#Declaramos las Variables
Temperatura =[]
Bucle = True
Opciones = 0
Promedio = 0
TemperaturaBaja = 0
TemperaturaAlta = 0

#Bienvenida 
while Bucle:
    Opciones=int(input('''Bienvenido al medidor de temperatura
            Elija por favor una opcion del menu
            1. Ingresar las temperaturas de la semana
            2. Muestre las temperaturas ingresadas, el promedio y en que dia ha sido mas alta y mas baja la temperatura.
            3. Salir del programa        
            '''))
    
    #Validacion de opciones correctas
    while Opciones != 1 and Opciones != 2 and Opciones != 3:
        print("Por favor ingrese un valor valido")
        Opciones=int(input('''Bienvenido al medidor de temperatura
            Elija por favor una opcion del menu
            1. Ingresar las temperaturas de la semana
            2. Muestre las temperaturas ingresadas, el promedio y en que dia ha sido mas alta y mas baja la temperatura.
            3. Salir del programa        
            '''))

    #Captura de opcion de ingreso # 1
    if Opciones == 1:
        #captura de datos de temperaturas de cada dia
        
        tempLun = int(input("ingrese la Temperatura del dia lunes: "))
        Temperatura.append(tempLun)
        tempMar = int(input("ingrese la temperatura del dia martes: "))
        Temperatura.append(tempMar)
        tempMier = int(input("ingrese la temperatura del dia Miercoles: "))
        Temperatura.append(tempMier)
        tempjuev = int(input("ingrese la temperatura del dia jueves: "))
        Temperatura.append(tempjuev)
        tempvier = int(input("ingrese la temperatura del dia viernes: "))
        Temperatura.append(tempvier)
        tempsab = int(input("ingrese la temperatura del dia sabado: "))
        Temperatura.append(tempsab)
        tempdom = int(input("Ingrese la temperatura del dia domingo"))
        Temperatura.append(tempdom)
    
        
    #informacion de calculo de min y max
    
        for i in range(0, len(Temperatura)):
            if Temperatura[i] == max(Temperatura):
                if i == 0:
                    TemperaturaAlta = "Lunes" 
                elif i == 1:
                    TemperaturaAlta == "Martes" 
                elif i == 2:
                    TemperaturaAlta == "Miercoles"
                elif i == 3:
                    TemperaturaAlta == "Jueves"
                elif i == 4:
                    TemperaturaAlta == "Viernes"
                elif i == 5:
                    TemperaturaAlta == "Sabado"  
                elif i == 6:
                    TemperaturaAlta == "Domingo"
                
            if Temperatura[i] == min(Temperatura):
                if i == 0:
                    TemperaturaBaja = "Lunes"
                elif i == 1:
                    TemperaturaBaja = "Martes"
                elif i == 2:
                    TemperaturaBaja = "Miercoles"
                elif i == 3:
                    TemperaturaBaja = "Jueves"
                elif i == 4:
                    TemperaturaBaja = "Viernes"
                elif i == 5:
                    TemperaturaBaja = "Sabado"
                elif i == 6:
                    TemperaturaBaja = "Domingo"
        Promedio = (tempLun + tempMar + tempMier + tempjuev + tempvier + tempsab + tempdom) / 7
    
    #Captura de opcion de ingreso # 2
    elif Opciones == 2:
        #Validacion de Ingreso en 0
        if len(Temperatura) == 0:
            print("No se han registrado temperaturas en el programa")
        #Se muestra primero valores ingresados para cada dia
        else:
            print(f'''se muestra a continuación el listado de temperaturas de cada dia
                    Lunes = {tempLun}
                    Martes = {tempMar}
                    Miercoles = {tempMier}
                    Jueves = {tempjuev}
                    Viernes = {tempvier}
                    sabado = {tempsab}
                    Domingo= {tempdom}
                    ''')
            #Se Muestra el promedio de las temperaturas
            print(f"el promedio de las temperaturas ingresado y mostrado anteriormente es {Promedio} Grados.")
            #Se muestra la temperatura altas
            print(f"La temperatura mas alta fue el dia {TemperaturaAlta}, siendo de {max(Temperatura)} Grados")
            print(f"La temperatura mas baja fue el dia {TemperaturaBaja}, Siendo de {min(Temperatura)} Grados")
            
    #Captura de opcion de ingreso # 3
    else:
        Bucle = False
        print("ha finalizado el programa, vuelva pronto")        

            



#Captura de datos de temperatura

