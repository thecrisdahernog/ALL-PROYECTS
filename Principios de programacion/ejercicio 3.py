''' escribe un programa que ayude a una persona a sumar sus gastos del dia
los gastos a sumar son transporte, alimento y ocio'''

Transporte = float(input("ingrese por favor su gasto de transporte: "))
Alimentacion = float(input("ingrese por favor su gasto de alimentacion: "))
Ocio = float(input("ingrese por favor su gasto de ocio: "))
GastoFinal = Transporte + Alimentacion + Ocio
print(f"el gasto total del dia de esta persona es: {GastoFinal}")