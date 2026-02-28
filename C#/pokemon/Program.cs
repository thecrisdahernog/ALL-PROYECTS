using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace pokemon
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string pokemon = "Charmander";
            string tipo = "Agua";
            string tipoEnemigo = "Hada";
            int nivel = 12;
            int vida = 45;

            Console.WriteLine($"pokemon: {pokemon}");
            Console.WriteLine($"tipo: {tipo}");
            Console.WriteLine($"Enemigo tipo: {tipoEnemigo}");

            Console.WriteLine("-----------------------------");

            if (tipo == "Fuego")
            {
                if (tipoEnemigo == "Hada" || tipoEnemigo == "Fuego")
                {
                    vida = vida - 15;
                    Console.WriteLine("Hace daño normal");                    
                }
                else if (tipoEnemigo == "Agua")
                {
                    Console.WriteLine("No hace daño");                    
                }else if(tipoEnemigo == "Planta")
                {
                    Console.WriteLine("lo mato");
                    vida = vida = 0;
                }else if (tipo == "Planta")
                {
                    if (tipoEnemigo == "Hada" && tipoEnemigo == "Planta")
                    {
                        vida = vida - 15;
                        Console.WriteLine("Hace daño normal");
                    }else if (tipoEnemigo == "Agua")
                    {
                        vida = 0;
                        Console.WriteLine("Lo mato");
                    }else if (tipoEnemigo == "Fuego")
                    {
                        Console.WriteLine("No le hace Daño");
                    }
                }
            }Console.WriteLine($"su vida es: {vida}");

        }
    }
}
