import os
import time

class Mascota:
    def __init__(self, nombre):
        self.nombre = nombre
        self.felicidad = 70
        self.hambre = 20
        self.energia = 100

    def ganar(self):
        global GameOver
        print(f"Felicidades, has subido todas las estadisticas de {self.nombre} ¡Has ganado el juego!")
        print(self.cara())
        GameOver = True
    
    def morir(self):
        global GameOver
        print(f"¡Oh no! {self.nombre} ha muerto de hambre...")
        print(f"FIN DEL JUEGO.")
        print(self.cara())
        GameOver = True

    def suicidio(self):
        global GameOver
        print(f"""Mi carta de suicidio:

Estoy aburrido.

firma: {self.nombre}.""")
        print(f"FIN DEL JUEGO.")
        print(self.cara())
        GameOver = True
        
    def enfermo(self):
        global GameOver
        print(self.cara())
        print(f"Oh no, {self.nombre} ha enfermado, tendra que ir al veterinatio por un largo tiempo...")
        print(f"FIN DEL JUEGO.")
        print(self.cara())
        GameOver = True

    def revisar_estado(self):
        if self.hambre < -20: self.hambre = -20
        if self.felicidad > 120: self.felicidad = 120
        if self.energia > 120: self.energia = 120

        if self.hambre >= 100:
            self.morir()
        elif self.felicidad <= 0:
            self.suicidio()
        elif self.energia <= 0:
            self.enfermo()
        
        if self.hambre <= 0 and self.felicidad >= 100 and self.energia >= 100:
            self.ganar()

    def comer(self):
        self.hambre -= 20
        self.energia -= 10
    def dormir(self):
        self.energia += 20
        self.felicidad -= 10
    def jugar(self):
        self.felicidad += 20
        self.hambre += 10

    def felicidad_info(self):
        if self.felicidad < 20:
            stat = "Deprimido/a."
        elif self.felicidad < 40:
            stat = "Triste."
        elif self.felicidad < 60:
            stat = "Aburrido/a."
        elif self.felicidad < 80:
            stat = "Feliz."
        elif self.felicidad < 100:
            stat = "Muy feliz."
        else:
            stat = "Extremadamente feliz."
        return stat
    def hambre_info(self):
        if self.hambre > 80:
            stat = "Muriendo de hambre."
        elif self.hambre > 60:
            stat = "Hambriento/a."
        elif self.hambre > 40:
            stat = "Neutral."
        elif self.hambre > 20:
            stat = "Bien."
        elif self.hambre > 0:
            stat = "Satisfecho/a."
        else:
            stat = "Lleno/a."
        return stat
    def energia_info(self):
        if self.energia < 20:
            stat = "Letargico/a."
        elif self.energia < 40:
            stat = "Cansado/a."
        elif self.energia < 60:
            stat = "Neutral."
        elif self.energia < 80:
            stat = "Muy energetico/a."
        elif self.energia < 100:
            stat = "Muy feliz."
        else:
            stat = "Saltando con energia."
        return stat
    
    def cara(self):
        estado = min(100 - self.hambre, self.felicidad, self.energia)
        if estado >= 100:
            return ":D"
        if estado >= 80:
            return ":)"
        if estado >= 60:
            return ":|"
        if estado >= 40:
            return "):"
        if estado >= 20:
            return "D:"
        elif estado >= 0:
            return "T-T"
        else:
            return "x_x"

    def info(self):
        cara = self.cara()
        print(f"""
                {cara}
==========Stats De {tamagochi.nombre}===========
Hambre: {self.hambre_info()}
Felicidad: {self.felicidad_info()}
Energia: {self.energia_info()}
""")
    def acciones(self):
        print(f"""
Selecciona una de las siguientes acciones:
1. Comer
2. Jugar
3. Dormir
""")
        seleccion = input()
        if seleccion == "1": 
            self.comer()
            os.system('cls')
            print(f"{self.nombre} está comiendo!")
            time.sleep(1.5)
            self.revisar_estado()
        elif seleccion == "2": 
            self.jugar()
            os.system('cls')
            print(f"{self.nombre} está jugando!")
            time.sleep(1.5)
            self.revisar_estado()
        elif seleccion == "3": 
            self.dormir()
            os.system('cls')
            print(f"{self.nombre} está durmiendo!")
            time.sleep(1.5)
            self.revisar_estado()
        else: 
            os.system('cls')
            print("Ese no es un comando valido.")
            time.sleep(1.5)
            self.revisar_estado()
    def medir_tiempo(self):
        global Tiempo
        tiempo_viejo = Tiempo
        Tiempo = time.time()
        daño_a_stats = Tiempo - tiempo_viejo
        self.energia -= daño_a_stats / 2
        self.felicidad -= daño_a_stats / 2
        self.hambre += daño_a_stats / 2
        

GameOver = False
Tiempo = time.time()
os.system('cls')
tamagochi = input("Ingrese el nombre de su mascota:")
tamagochi = Mascota(tamagochi)
while GameOver == False:
    tamagochi.medir_tiempo()
    Tiempo = time.time()

    tamagochi.info()
    tamagochi.acciones()