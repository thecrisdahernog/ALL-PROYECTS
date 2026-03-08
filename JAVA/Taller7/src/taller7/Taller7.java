/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package taller7;

import java.util.Scanner;

/**
 *
 * @author Dell
 */
public class Taller7 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        double peso,estatura,imc;
        System.out.println("Bienvenidos al calculador del IMC");
        System.out.println("Ingrese por favor su peso en kilogramos: ");
        peso = leer.nextDouble();
        System.out.println("Ingrese su estatura en metros: ");
        estatura = leer.nextDouble();
        imc = peso / Math.pow(estatura, 2);
        
    }
    
}
