using System.Diagnostics;
using System.Timers;

int Diasemana = 0;

Console.WriteLine("Introduce un numero: ");
Diasemana = int.Parse(Console.ReadLine());

string mensaje = Diasemana == 1 ? "El dia de hoy es lunes" : Diasemana == 2 ? "El dia de hoy es Martes" : Diasemana == 3 ? "El dia de hoy es Miercoles"
    : Diasemana == 4 ? "El dia de hoy es Jueves" : Diasemana == 5 ? "El dia de Hoy es Viernes" : Diasemana == 6 ? "El dia de hoy es Sabado" : Diasemana == 7 ? "El dia de hoy es Domingo" : Diasemana > 8 ? "Es un dia de semana que no existe" : Diasemana <= 0 ? "Es un dia de semana que no existe" : "" ;
Console.WriteLine(mensaje);