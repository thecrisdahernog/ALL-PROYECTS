using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Ciclos
{
    internal class Program
    {
        static void Main(string[] args)
        {
            //int edad = 18;
            //for (int i = 1; i < edad; i++) 
            //{
            //    Console.WriteLine($"tienes {i} años. estas creciendo");
            //}
            //Console.WriteLine("Eres mayor de edad");

            int edad = 18;
            for (int i = 1; i < edad; i++)
            {
                
                if (i == 15)
                {
                    continue;
                }
                Console.WriteLine($"tienes {i} años. estas creciendo");
            }
            Console.WriteLine("eres mayor de edad");

            //int edad;
            //while (true)
            //{
            //    Console.WriteLine("Introduce tu edad");
            //    edad = int.Parse(Console.ReadLine());
            //    if (edad == 0)
            //    {
            //        break; 
            //    }
            //    else
            //    {
            //        Console.WriteLine("Edad ingresada al sistema");
            //    }

        }
    }
    
}
