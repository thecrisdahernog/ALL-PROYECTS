import os
os.system('cls')

class Cuenta_Bancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        
    def depositar(self, monto):
        if monto <= 0:
            print("Introduzca un valor valido")
        else: 
            self.saldo = self.saldo + monto
            print("se depositaron: ", monto)
            
        def retirar(self, monto):
            if monto >= 0:
                print("Introduzca un valor valido")
            elif monto > self.saldo:
                print("saldos insuficientes.")
            else:
                self.saldo = self.saldo = monto
                
        
        

cuenta1 = Cuenta_Bancaria("Yeiner",19900)
cuenta2 = Cuenta_Bancaria("Valentina",0)

#Depositar
print("usuario intenta depositar 20000")

#retirar
print("")