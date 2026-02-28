/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package suma.de.numeros;

import java.util.Scanner;

/**
 *
 * @author Dell
 */
public class SumaDeNumeros {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        System.out.println("Ingrese el primer Numero: ");
        int Num1 = leer.nextInt();
        System.out.println("Ingrese el Segundo Numero");
        int Num2 = leer.nextInt();
        int resultado = Num1 + Num2;
        System.out.println("El resultado de la suma es: "+ resultado);
    }
    
}
