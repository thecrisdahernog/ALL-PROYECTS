using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CapturadorSueldo
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int HorasTrabajadas;
            double CostoHoras;
            double sueldo;
            Console.WriteLine("Ingrese la cantidad de horas trabajadas");
            HorasTrabajadas = int.Parse(Console.ReadLine());
            Console.WriteLine("Cuanto es el valor de las horas");
            CostoHoras = int.Parse(Console.ReadLine());
            
            sueldo = HorasTrabajadas * CostoHoras;

            Console.WriteLine($"El sueldo que vas a devengar es: {sueldo}");
        }
    }
}
