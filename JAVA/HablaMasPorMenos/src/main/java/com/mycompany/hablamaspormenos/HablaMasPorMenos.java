/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.hablamaspormenos;

import java.util.Scanner;

/**
 *
 * @author Dell
 */
public class HablaMasPorMenos {

    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        int minutos,dia;
        double costo;
        System.out.println("elija por favor el dia de la semana actual: ");
        System.out.println("1.Lunes\n2.Martes\n3.Miercoles\n4.Jueves\n5.Viernes\n6.Sabado\n7.Domingo");
        dia = leer.nextInt();
        System.out.println("Ingrese la cantidad de minutos hablados");
        minutos = leer.nextInt();
        
    }
}
