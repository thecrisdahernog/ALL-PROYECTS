import os
os.system('cls')

class Producto:
    def __init__(self, nombre, precio, stock):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        
    def mostrar_producto(self):
        print("El articulo: ", self.nombre)
        print("El precio del articulo es: ", self.precio)
        print("La cantidad de articulos de inventario es: ", self.stock)
        
    def Vender_producto(self, cantidad):
        if cantidad > self.stock:
            print("No hay suficiente stock para completar la venta.")
        else:
            self.stock = self.stock - cantidad
            total = self.precio * cantidad
            print(f"Se han vendido {cantidad} unidades de {self.nombre}. Total: {total}")
            
producto1 = Producto("Camiseta", 20, 100)
producto2 = Producto("Pantalon", 40, 50)
producto1.mostrar_producto()
producto2.mostrar_producto()

producto1.Vender_producto(10)
producto2.Vender_producto(60)

producto1.mostrar_producto()
producto2.mostrar_producto()
        
    