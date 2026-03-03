import os
os.system('cls')

from Habitacion_simple import Habitacion_Simple
from habitacion_suite import Habitacion_suite

habitacion1 = Habitacion_Simple(101, 25000, 1)
habitacion2 = Habitacion_suite(201, 30000, False)
habitacion3 = Habitacion_suite(202, 40000, True)

habitacion1.mostrar_info()
habitacion2.mostrar_info()
habitacion3.mostrar_info()

habitacion1.descripcion()
habitacion2.descripcion()
habitacion3.descripcion()