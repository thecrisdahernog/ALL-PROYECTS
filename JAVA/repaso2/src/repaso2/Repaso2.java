/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package repaso2;

import java.util.Scanner;

/**
 *
 * @author Dell
 */
public class Repaso2 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        double ValorHora,HoraTrabajo,salario,aumento;
        System.out.println("Bienvenidos al programa de revision de salario.");
        System.out.println("Ingrese por favor la cantidad de horas trabajadas: ");
        HoraTrabajo = leer.nextFloat();
        System.out.println("Ingrese el valor de la Hora laboral:");
        ValorHora = leer.nextFloat();
        salario = HoraTrabajo*ValorHora;
        if (HoraTrabajo >= 40){
            aumento = (salario *1.50);
            System.out.println("has trabajado mas de 40 Horas, mereces un aumento");
            System.out.println("El valor total de ese aumento es "+salario);
            
        }else{
            System.out.println("El valor total a pagar al trabajador es: "+salario);
        }
    }
    
}
