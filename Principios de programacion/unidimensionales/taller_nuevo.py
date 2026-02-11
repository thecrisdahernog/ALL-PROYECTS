#encuesta de satisfaccion de clientes

import os
os.system('cls')

#Declaracion de variables
Clientes = []
Edades = []
calificaciones = []
Promedio = []
Bucle = True
Opciones = 0
Satisfechos = 0
Aceptables = 0
Insatisfechos = 0

while Bucle: 
    
    Opciones = int(input('''
                            === Bienvenido a la encuesta de satisfaccion de los clientes ===
                            
                            Elija por favor una de las siguientes opciones:
                            1. realizar una encuesta
                            2. revisar encuesta
                            3. realizar informe general de encuesta
                            4. salir del programa
                            --> 
                            '''))
    while Opciones != 1 and Opciones != 2 and Opciones != 3 and Opciones != 4:
        print("Eligio una opcion invalida del menu")
        
        Opciones = int(input('''
                            === Bienvenido a la encuesta de satisfaccion de los clientes ===
                            
                            Elija por favor una de las siguientes opciones:
                            1. realizar una encuesta
                            2. revisar encuesta
                            3. realizar informe general de encuesta
                            4. salir del programa
                            --> 
                            '''))
    if Opciones == 1:
        
        Nombre = input("para iniciar, ingrese por favor su nombre: ")
        while Nombre == "":
            Nombre = input("Ingrese por favor un nombre valido: ")
        Clientes.append(Nombre)
    
        Edad = int(input("ingrese por favor su edad: "))
        while Edad < 0 and Edad == "":
            Edad = int(print("Ingrese por favor una edad Valida: "))
        Edades.append(Edad)
        
        Servicio = int(input("Ingrese como le ha parecido el servicio, con una calificacion entre 0 - 5: "))
        while Servicio < 0 or Servicio > 5:
            Servicio = int(input("Ingrese por favor una Calificacion valida, que este en el rango entre 0 - 5: "))
        calificaciones.append(Servicio)
        
        Calidad = int(input("Ingrese como le ha parecido la calidad de los productos, con una calificacion entre 0 - 5: "))
        while Calidad  < 0 or Calidad >5:
            Calidad = int(input("Ingrese por favor una calificacion validad, que este en el rango entre 0 - 5: "))
        calificaciones.append(Calidad)
        
        Precio = int(input("Ingrese como le ha parecido los precios, con una calificacion entre  0 - 5: "))
        while Precio < 0 or Precio >5:
            Precio = int(input("ingrese por favor una calificacion valida, que este en el rango entre 0 - 5: "))
        calificaciones.append(Precio)
            
        Promedio.append((Servicio+Calidad+Precio)/3)
        print("La encuesta fue ingresada correctamente")        
    elif Opciones == 2:
        
        if len(Clientes) == 0:
            print("no Hay Clientes registrados")
            
        else: 
            for i in range(len(Clientes)):
                print(f'''{Clientes[i]}
{Edades[i]}
                        ''')
                for e in range(len(calificaciones)):
                    if e >= i * 3 and e <= i * 3 + 2:
                        print(calificaciones[e])
                        
    elif Opciones == 3:
        for i in (Promedio):
            if i > 4:
                Satisfechos += 1
            elif i > 3:
                Aceptables += 1
            else:
                Insatisfechos += 1
        print(f"Los clientes que quedaron satisfechos con nuestros servicios son: {Satisfechos}")
        print(f"Los clientes que consideran aceptable nuestro servicion son: {Aceptables}")
        print(f"Los clientes que quedaron insatisfechos con nuestro servicios son: {Insatisfechos}")
    else:
        Bucle == False


