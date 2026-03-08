/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package taller6;

import java.util.Scanner;

/**
 *
 * @author Dell
 */
public class Taller6 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        double capital,tasainteres,años,montofinal;
        System.out.println("Bienvenido al programa para determinar su monto final");
        System.out.println("Ingrese por favor su capital invertido para hacer el calculo: ");
        capital = leer.nextDouble();
        System.out.println("ingrese el porcentaje de la tasa del interes anual: ");
        tasainteres = leer.nextDouble();
        tasainteres = tasainteres / 100;
        System.out.println("Ingrese por favor el numero de años, para el calculo: ");
        años = leer.nextDouble();
        montofinal = capital * Math.pow(1 + tasainteres, años);
        System.out.println("su monto final es de: "+montofinal);
        if(montofinal>(capital*1.50)){
            System.out.println("La ganancia del monto final supera el 50% de su capital inicial");
        }else{
            System.out.println("La ganancia del monto final no supera el 50% de su capital inicial");
        }
    }
    
}
