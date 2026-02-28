using System.Diagnostics;

int edad = 0;

Console.WriteLine("Introduce tu edad: ");
edad = int.Parse(Console.ReadLine());

string mensaje = edad >= 18  ? "Eres mayor de edad" : "Vayase de aqui pelaito";
Console.WriteLine(mensaje);
