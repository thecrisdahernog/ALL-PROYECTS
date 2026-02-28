using System;
using System.Collections.Generic;
using System.ComponentModel.Design;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FastCode_Burgers
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int menu;
            int opciones;
            double Total;
            int Clasica = 5;
            int Doble = 7;
            int full = 9;
            int refresco = 2;
            int Cantidad;
            int Acumulado = 0;
            bool Salir = true;

            while(Salir) { 
                Console.WriteLine("==============================");
                Console.WriteLine("Bienvenidos a fastcode burgers");
                Console.WriteLine("==============================");
                Console.WriteLine("Elija una de las siguientes opciones");
                Console.WriteLine("1.Mostrar Menu \n 2.Mostrar total de factura");
                opciones = int.Parse(Console.ReadLine());
                if (opciones == 1)
                {
                    Console.WriteLine("==============================");
                    Console.WriteLine("Menu:");
                    Console.WriteLine("==============================");
                    Console.WriteLine("Hamburguesas: \n 1.Bug-Free Burger - clasica ($5) \n 2. Syntax Stack - Doble carne ($7) \n 3. Full-Stack Burguer - Extra grande ($9) \n Bebidas: \n 4. Refresco ($2)");
                    menu = int.Parse(Console.ReadLine());
                    if (menu == 1)
                    {
                        Console.WriteLine("Ingrese la cantidad a llevar: ");
                        Cantidad = int.Parse(Console.ReadLine());
                        Acumulado += Clasica * Cantidad;
                        Console.WriteLine($"El acumulado de la factura es: {Acumulado}");
                    }
                    else if (menu == 2)
                    {
                        Console.WriteLine("Ingrese la cantidad a llevar: ");
                        Cantidad = int.Parse(Console.ReadLine());
                        Acumulado += Doble * Cantidad;
                        Console.WriteLine($"El acumulado de la factura es: {Acumulado}");
                    }
                    else if (menu == 3)
                    {
                        Console.WriteLine("Ingrese la cantidad a llevar: ");
                        Cantidad = int.Parse(Console.ReadLine());
                        Acumulado += full * Cantidad;
                        Console.WriteLine($"El acumulado de la factura es: {Acumulado}");
                    }
                    else if (menu == 4)
                    {
                        Console.WriteLine("Ingrese la cantidad a llevar: ");
                        Cantidad = int.Parse(Console.ReadLine());
                        Acumulado += refresco * Cantidad;
                        Console.WriteLine($"El acumulado de la factura es: {Acumulado}");
                    }
                }else
                {
                    Total = Acumulado;
                    if (Total >= 20)
                    {
                        Console.WriteLine($"El total a pagar es: {Total}");
                        Total = Total * 0.90;                        
                        Console.WriteLine($"Se realizo un descuento de 10% y su total a pagar es: ${Total}");
                        Console.WriteLine("Muchas gracias por su compra, vuelva Pronto");
                        Salir = false;
                    }else
                    {
                        Console.WriteLine($"El total a pagar es: {Total}");
                        Console.WriteLine("Muchas gracias por su compra, vuelva Pronto");
                        Salir = false;
                    }
                }
                
            }

        }
    }
}
