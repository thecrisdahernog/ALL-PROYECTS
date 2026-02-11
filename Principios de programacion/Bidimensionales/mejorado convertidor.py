import os
from typing import List, Dict, Tuple
from decimal import Decimal, ROUND_HALF_UP

class CurrencyConverter:
    def __init__(self):
        self.exchange_rates = [    
            [1, 0.86, 18.43, 3880, 0.76],
            [1.16, 1, 21.46, 4536, 0.88],
            [0.047, 0.054, 1, 211.27, 0.041],
            [0.00026, 0.00022, 0.0047, 1, 0.00019],
            [1.31, 1.44, 3042, 1.00, 1]     
        ]
        self.currencies = ["USD", "EUR", "MEX", "COP", "GBP"]

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def format_currency(self, amount: float) -> str:
        """Format currency amounts with 2 decimal places"""
        return str(Decimal(str(amount)).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP))

    def display_menu(self) -> int:
        """Display main menu and return user choice"""
        menu = """
    Bienvenido al Convertidor de Divisas Internacional
    ================================================
    1. Convertir divisas
    2. Listar tasas de cambio
    3. Salir
    ================================================
    """
        while True:
            try:
                self.clear_screen()
                print(menu)
                choice = int(input("=> Seleccione una opción: "))
                if 1 <= choice <= 3:
                    return choice
                print("Por favor seleccione una opción válida (1-3)")
            except ValueError:
                print("Por favor ingrese un número válido")
            input("Presione Enter para continuar...")

    def currency_menu(self) -> int:
        """Display currency selection menu and return user choice"""
        menu = """
            |===========================|
            |   CONVERTIDOR DE DIVISAS  |
            |===========================|"""
        
        for i, currency in enumerate(self.currencies, 1):
            menu += f"\n            | {i}. {currency:<20} |"
        
        menu += "\n            |===========================|"
        
        while True:
            try:
                print(menu)
                choice = int(input("=> Seleccione una moneda: "))
                if 1 <= choice <= len(self.currencies):
                    return choice
                print(f"Por favor seleccione una opción válida (1-{len(self.currencies)})")
            except ValueError:
                print("Por favor ingrese un número válido")

    def get_amount(self, currency: str) -> float:
        """Get and validate amount to convert"""
        while True:
            try:
                amount = float(input(f"Ingrese el monto en {currency}: "))
                if amount >= 0:
                    return amount
                print("Por favor ingrese un monto positivo")
            except ValueError:
                print("Por favor ingrese un número válido")

    def convert_currency(self):
        """Handle currency conversion process"""
        from_currency = self.currency_menu()
        print("\nSeleccione la moneda a la que desea convertir:")
        to_currency = self.currency_menu()
        
        amount = self.get_amount(self.currencies[from_currency-1])
        rate = self.exchange_rates[from_currency-1][to_currency-1]
        result = amount * rate
        
        print("\nResultado de la conversión:")
        print("=" * 50)
        print(f"{self.format_currency(amount)} {self.currencies[from_currency-1]} = "
              f"{self.format_currency(result)} {self.currencies[to_currency-1]}")
        print(f"Tasa de cambio: 1 {self.currencies[from_currency-1]} = "
              f"{self.format_currency(rate)} {self.currencies[to_currency-1]}")
        print("=" * 50)

    def display_rates(self):
        """Display all exchange rates"""
        print("\nTasas de Cambio Actuales:")
        print("=" * 60)
        for i, from_curr in enumerate(self.currencies):
            print(f"\nTasas para {from_curr}:")
            print("-" * 40)
            for j, to_curr in enumerate(self.currencies):
                if i != j:
                    rate = self.exchange_rates[i][j]
                    print(f"1 {from_curr} = {self.format_currency(rate)} {to_curr}")
        print("=" * 60)

    def run(self):
        """Main application loop"""
        while True:
            choice = self.display_menu()
            
            if choice == 1:
                self.convert_currency()
            elif choice == 2:
                self.display_rates()
            else:
                print("\n¡Gracias por usar el Convertidor de Divisas!")
                break
            
            input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    converter = CurrencyConverter()
    converter.run()