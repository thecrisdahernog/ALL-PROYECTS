using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AccesoVIP
{
    internal class Program
    {
        static void Main(string[] args)
        {
            int edad;
            int Invitacion;
            int Lista;
            int Vestimenta;
            
            Console.WriteLine("Bienvenidos al Sistema de acceso al evento");
            Console.WriteLine("Responde las Siguientes preguntas para determinar tu ingreso al evento VIP");
            Console.WriteLine("Ingrese su edad:");
            edad = int.Parse(Console.ReadLine());
            if (edad >= 18)
            {
                Console.WriteLine("Tienes edad para ingresar al evento");
                Console.WriteLine("Cuentas con invitacion para este evento?");
                Console.WriteLine("responde 1.si - 2.no");
                Invitacion = int.Parse(Console.ReadLine());
                if (Invitacion == 1)
                {
                    Console.WriteLine("Si cuentas con invitacion, continuemos con el formulario");
                }else 
                {
                    Console.WriteLine("No cuentas con invitacion, pero estas en la lista VIP?");
                    Console.WriteLine("responde 1.si - 2.no");
                    Lista = int.Parse(Console.ReadLine());
                    if (Lista == 1) 
                    {
                        Console.WriteLine("Estas en lista VIP, continuemos con el formulario");
                        Console.WriteLine("IDentifica del siguiente listado cual es tu vestimenta");
                        Console.WriteLine("1. Formal \n 2.Semiformal \n 3.Informal");
                        Vestimenta = int.Parse(Console.ReadLine());
                        if (Vestimenta == 1)
                        {
                            Console.WriteLine("Cuentas con el codigo de vestimenta correcto, puedes ingresar al evento");
                        }
                        else
                        {
                            Console.WriteLine("No cuentas con el codigo de vestimenta correcto, NO puedes ingresar, por favor retirate");
                        }
                    }
                    else
                    {
                        Console.WriteLine("Tampoco estas en la Lista VIP, por favor retirate, no insistas");
                    }
                }
            }else
            {
                Console.WriteLine("No tienes edad para ingresar al evento, por favor retirate");
            }

        }
    }
}
