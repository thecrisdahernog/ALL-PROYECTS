/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package taller3;

import java.util.Scanner;

public class Taller3 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        double a,b,c,d,x;
        System.out.println("Ingrese el primer numero para la operación: ");
        a = leer.nextDouble();
        System.out.println("Ingrese el Segundo numero para la operación: ");
        b = leer.nextDouble();
        System.out.println("Ingrese el Tercer numero para la operación: ");
        c = leer.nextDouble();
        d = Math.pow(b, 2) - 4* (a*c);
        System.out.println("El discriminante es : "+d);
        
        if (Double.isNaN(Math.sqrt(d))){
            System.out.println("El discriminante no presenta raiz cuadrada");
        }else{
            x = (-b + Math.sqrt(d))/(2*a);
            System.out.println(x);
            x = (-b - Math.sqrt(d))/(2*a);
            System.out.println(x);
        }
    }
    
}
