using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace primerospasos2
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int edad;
            string nombre = "Cristian";
            bool mayoredad = true;
            double estatura = 1.6;
            float estatura2 = 1.0f;

            Console.WriteLine("Introduce una edad porfavorcito: ");
            edad = int.Parse(Console.ReadLine());

            if (mayoredad)
            {
                Console.WriteLine("Hola Mundo 2");
            }
            else if (edad > 27)
            {
                Console.WriteLine("Mundo 2");
            }
            else if (edad < 27)
            {
                Console.WriteLine("2");
            }
            else
            {
                Console.WriteLine("Adios Mundo 2");
            }
        }
    }
}
