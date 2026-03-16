import os
os.system('cls')

from caza import Caza
from crucero import Crucero

nave1 = Caza("cazador 1",100,20,100)
nave2 = Crucero("Alfa 5",100,20,True)

while nave1.vida > 0 and nave2.vida > 0:
    nave1.disparar(nave2)
    nave2.mostrar_estado()
    if nave2.vida > 0:
        nave2.disparar(nave1)
        nave1.mostrar_estado()