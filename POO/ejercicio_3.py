#tienes dos listas de jugadores:
#equipo a: {"Ana","Luis","pedro","Marta","Sofia"}
#equipo b: {"Pedro","Sofia","Carlos","Lucia","Javier"}
#1. Jugadores que estan en ambos equipos
#2. Jugadores unicos de cada equipo
#3.Todos los jugadores sin duplicados
import os
os.system('cls')

A = {"Ana","Luis","Pedro","Marta","Sofia"}
B = {"Pedro","Sofia","Carlos","Lucia","Javier"}

print(f"Los jugadores que estan en ambos equipos son: {A&B}")
print(f"Los jugadores unicos de cada equipo: {A-B}")
print(f"Todos los jugadores sin duplicados: {A^B}")
