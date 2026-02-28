using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AcademiaDeMagos
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string Nombre;
            int Aprendices;
            int PoderMAgico;
            int ControlHechizo;
            int Estrategia;
            int PromedioGeneral;
            int PromedioAprendis;
            int PromedioAcumulado = 0;
            int Archimago = 0;
            int MagoAvanzado = 0;
            int Aprendiz = 0;
            int Expulsado = 0;

            Console.WriteLine("Bienvenidos a la academia de magos");
            Console.WriteLine("Ingrese por favor el numero de aprendices: ");
            Aprendices = int.Parse(Console.ReadLine());
            for (int i = 0; i < Aprendices; i++)
            {
                Console.WriteLine($"Ingrese el nombre del {i+1} Mago");
                Nombre = Console.ReadLine();
                Console.WriteLine($"Ingrese el poder magico del {i + 1} Mago (o-100)");
                PoderMAgico = int.Parse(Console.ReadLine());
                Console.WriteLine($"Ingrese el control de hechizo del {i + 1} Mago (0-100)");
                ControlHechizo = int.Parse(Console.ReadLine());
                Console.WriteLine($"Ingrese su nivel de estrategia del {i + 1} Mago (0-100)");
                Estrategia = int.Parse(Console.ReadLine());

                PromedioAprendis = (PoderMAgico + ControlHechizo + Estrategia) / Aprendices;
                Console.WriteLine($"El promedio de este aprendis es: {PromedioAprendis}");
                PromedioAcumulado = PromedioAcumulado + PromedioAprendis;

                if (PromedioAprendis >= 90)
                {
                    Console.WriteLine("LA Categoria de este mago es: Archimago");
                    Archimago++;
                }
                else if (PromedioAprendis >= 70)
                {
                    Console.WriteLine("La Categoria de este mago es: MagoAvanzado");
                    MagoAvanzado++;
                }else if (PromedioAprendis >= 50)
                {
                    Console.WriteLine("La Categoria de este mago es: Aprendiz");
                    Aprendiz++;
                }
                else
                {
                    Console.WriteLine("La Categoria de este Mago es: Expulsado");
                    Expulsado++;
                }
                


            }
            
            PromedioGeneral = PromedioAcumulado / Aprendices;
            Console.WriteLine($"El promedio general de la academia es: {PromedioGeneral}");
            Console.WriteLine($"El total de aprendices Archimagos es: {Archimago}");
            Console.WriteLine($"El total de aprendices Expulsados es: {Expulsado}");
        }
    }
}
