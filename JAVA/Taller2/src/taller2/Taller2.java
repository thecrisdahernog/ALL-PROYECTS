/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package taller2;

import java.util.Scanner;

/**
 *
 * @author Dell
 */
public class Taller2 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner leer = new Scanner (System.in);
        int edad,edadmeses,edaddias,edadhoras;
        System.out.println("Iniciamos el programa de Revision de edades");
        System.out.println("ingrese por favor su edad: ");
        edad = leer.nextInt();
        edadmeses = edad * 365;
        edaddias = edadmeses * 30;
        edadhoras = edaddias * 24;
        System.out.println("segun su edad usted ha vivido "+edadmeses+" meses, "+edaddias+" dias y "+edadhoras+" Horas aproximadamente.");
    }
    
}
