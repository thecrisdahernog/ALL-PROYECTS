/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package repaso4;

import java.util.Scanner;

/**
 *
 * @author Dell
 */
public class Repaso4 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
       Scanner leer = new Scanner(System.in);
       int edad;
        System.out.println("Revision de edades para votacion");
        System.out.println("ingrese su edad: ");
        edad = leer.nextInt();
        if (edad>=18){
            System.out.println("Ya eres mayor de edad, puedes ejercer tu derecho al voto");
        }else{
            System.out.println("No eres mayor de edad, no puede votar aun");
        }
    }
    
}
