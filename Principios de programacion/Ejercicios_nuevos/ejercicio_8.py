import random
from collections import defaultdict
import os

class SimuladorDados:
    def __init__(self):
        self.lanzamientos = []
        self.contador_sumas = defaultdict(int)
        self.contador_pares = 0
        self.total_lanzamientos = 0
        
    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def obtener_cantidad_lanzamientos(self) -> int:
        """Solicita y valida la cantidad de lanzamientos"""
        while True:
            try:
                cantidad = int(input("¿Cuántas veces desea lanzar los dados? => "))
                if cantidad <= 0:
                    print("Por favor ingrese un número positivo.")
                    continue
                if cantidad > 1000000:
                    print("El número es muy grande. Máximo 1,000,000 lanzamientos.")
                    continue
                return cantidad
            except ValueError:
                print("Por favor ingrese un número entero válido.")
    
    def lanzar_dados(self) -> tuple:
        """Simula el lanzamiento de dos dados"""
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        return dado1, dado2
    
    def realizar_lanzamientos(self):
        """Realiza todos los lanzamientos y registra los datos"""
        print(f"\nRealizando {self.total_lanzamientos} lanzamientos...")
        
        for _ in range(self.total_lanzamientos):
            dado1, dado2 = self.lanzar_dados()
            suma = dado1 + dado2
            
            # Registrar el lanzamiento
            self.lanzamientos.append((dado1, dado2, suma))
            self.contador_sumas[suma] += 1
            
            # Contar si es un par
            if dado1 == dado2:
                self.contador_pares += 1
        
        print("✓ Lanzamientos completados.\n")
    
    def calcular_estadisticas(self):
        """Calcula las estadísticas de los lanzamientos"""
        # Encontrar la suma más frecuente
        suma_frecuente = max(self.contador_sumas, key=self.contador_sumas.get)
        frecuencia_maxima = self.contador_sumas[suma_frecuente]
        
        # Calcular porcentajes
        porcentajes = {}
        for suma in range(2, 13):
            if suma in self.contador_sumas:
                porcentaje = (self.contador_sumas[suma] / self.total_lanzamientos) * 100
                porcentajes[suma] = porcentaje
            else:
                porcentajes[suma] = 0.0
        
        # Porcentaje de pares
        porcentaje_pares = (self.contador_pares / self.total_lanzamientos) * 100
        
        return suma_frecuente, frecuencia_maxima, porcentajes, porcentaje_pares
    
    def mostrar_reporte(self):
        """Muestra el reporte final con todas las estadísticas"""
        suma_frecuente, frecuencia_maxima, porcentajes, porcentaje_pares = self.calcular_estadisticas()
        
        self.limpiar_pantalla()
        print("=" * 70)
        print(" " * 15 + "REPORTE FINAL - SIMULADOR DE DADOS")
        print("=" * 70)
        
        # Resumen general
        print(f"\nRESUMEN GENERAL:")
        print("-" * 70)
        print(f"Total de lanzamientos: {self.total_lanzamientos:,}")
        print(f"Total de pares obtenidos: {self.contador_pares:,}")
        print(f"Porcentaje de pares: {porcentaje_pares:.2f}%")
        print(f"Suma más frecuente: {suma_frecuente} (apareció {frecuencia_maxima:,} veces)")
        
        # Tabla de distribución
        print(f"\nDISTRIBUCIÓN DE SUMAS:")
        print("-" * 70)
        print(f"{'Suma':<6} {'Frecuencia':<15} {'Porcentaje':<15} {'Visualización':<40}")
        print("-" * 70)
        
        for suma in range(2, 13):
            frecuencia = self.contador_sumas[suma]
            porcentaje = porcentajes[suma]
            # Crear una barra visual
            barra = "█" * int(porcentaje / 2)
            print(f"{suma:<6} {frecuencia:<15,} {porcentaje:>6.2f}%        {barra}")
        
        # Análisis detallado de pares
        print(f"\nANÁLISIS DE PARES:")
        print("-" * 70)
        print(f"{'Dado (1,1) (2,2)...':<20} {'Cantidad':<15}")
        print("-" * 70)
        
        pares_encontrados = defaultdict(int)
        for dado1, dado2, _ in self.lanzamientos:
            if dado1 == dado2:
                pares_encontrados[dado1] += 1
        
        for numero in range(1, 7):
            cantidad = pares_encontrados[numero]
            print(f"({numero},{numero})              {cantidad:>15,}")
        
        # Estadísticas interesantes
        print(f"\nESTADÍSTICAS INTERESANTES:")
        print("-" * 70)
        suma_minima = min(self.contador_sumas, key=self.contador_sumas.get)
        suma_minima_frecuencia = self.contador_sumas[suma_minima]
        
        suma_maxima_valor = max(self.contador_sumas, key=self.contador_sumas.get)
        suma_maxima_frecuencia = self.contador_sumas[suma_maxima_valor]
        
        print(f"Suma con menor frecuencia: {suma_minima} ({suma_minima_frecuencia:,} veces)")
        print(f"Suma con mayor frecuencia: {suma_maxima_valor} ({suma_maxima_frecuencia:,} veces)")
        print(f"Diferencia: {suma_maxima_frecuencia - suma_minima_frecuencia:,} lanzamientos")
        
        # Promedio teórico vs práctico
        promedio_teorico = 7.0
        suma_total = sum(suma * frecuencia for suma, frecuencia in self.contador_sumas.items())
        promedio_practico = suma_total / self.total_lanzamientos
        
        print(f"\nPromedio teórico de suma: {promedio_teorico:.2f}")
        print(f"Promedio práctico de suma: {promedio_practico:.2f}")
        print(f"Diferencia: {abs(promedio_practico - promedio_teorico):.4f}")
        
        print("\n" + "=" * 70)
    
    def ejecutar(self):
        """Ejecuta el simulador completo"""
        self.limpiar_pantalla()
        print("╔════════════════════════════════════════════════════════════════════╗")
        print("║          SIMULADOR DE LANZAMIENTO DE DADOS                        ║")
        print("╚════════════════════════════════════════════════════════════════════╝\n")
        
        # Obtener cantidad de lanzamientos
        self.total_lanzamientos = self.obtener_cantidad_lanzamientos()
        
        # Realizar lanzamientos
        self.realizar_lanzamientos()
        
        # Mostrar reporte
        self.mostrar_reporte()
        
        # Opción de guardar reporte
        while True:
            opcion = input("\n¿Desea realizar otra simulación? (S/N): ").upper()
            if opcion in ['S', 'N']:
                break
            print("Por favor ingrese S o N")
        
        if opcion == 'S':
            self.lanzamientos = []
            self.contador_sumas = defaultdict(int)
            self.contador_pares = 0
            self.total_lanzamientos = 0
            self.ejecutar()
        else:
            print("\n¡Gracias por usar el simulador de dados!")

def main():
    simulador = SimuladorDados()
    simulador.ejecutar()

if __name__ == "__main__":
    main()











