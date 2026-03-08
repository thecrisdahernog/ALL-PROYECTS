/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.taller1;

import java.util.Scanner;

/**
 *
 * @author Dell
 */
public class Taller1 {

    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        long SalarioBase,CalculoHora,CalculoExtra,TotalConExtra,TotalDescuento,TotalFinal;
        int HorasExtrasTrabajos;
        System.out.println("Bienvenido al Sistema de revision de horas extras");
        System.out.println("para determinar cuanto aplica en su salario las horas extras necesitamos los siguientes datos");
        System.out.println("Ingrese por favor su salario base");
        SalarioBase = leer.nextLong();
        CalculoHora = SalarioBase / 240;
        CalculoExtra = (long) (CalculoHora * 1.25);
        System.out.println("Segun su salario, el valor de su hora ordinaria es "+CalculoHora+" y el valor de su hora extra es de: "+CalculoExtra);
        System.out.println("Ingrese por favor La cantidad de horas extras trabajadas en este mes: ");
        HorasExtrasTrabajos = leer.nextInt();
        TotalConExtra = HorasExtrasTrabajos * CalculoExtra;
        TotalFinal = TotalConExtra + SalarioBase;
        System.out.println("el Total de su pago con Horas extras incluidas es de: "+TotalFinal);
        if (TotalFinal >= 5000000){
            TotalDescuento = (long) (TotalFinal * 0.90);
            System.out.println("Al tener un salario igual o superior a 5.000.000 se hace descuento de un 10% en regalias");
            System.out.println("Su salario final es: "+TotalDescuento);
        }
        
        
        
    }
}
