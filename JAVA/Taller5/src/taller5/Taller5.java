/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package taller5;

import java.util.Scanner;



/**
 *
 * @author Dell
 */
public class Taller5 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        double consumo,costo,totalconsumo;
        System.out.println("Bienvenido al programa ára determinar su pago de energia");
        System.out.println("Ingrese por favor la cantidad de kWh consumidas: ");
        consumo = leer.nextDouble();
        System.out.println("Ingrese por favor el valor del Kwh: ");
        costo = leer.nextDouble();
        totalconsumo = consumo * costo;
        System.out.println("El valor total a pagar de su factura es de: "+totalconsumo);
        if (consumo<100){
            System.out.println("Al tener un consumo menor a 100 Kwh tiene un descuento del 15% de descuento");
            totalconsumo = totalconsumo * 0.85;
            System.out.println("El valor total a pagar de su factura es de: "+totalconsumo);
        }else if (consumo>500){
            System.out.println("Al tener un consumo mayor a 500 kWh tiene un recargo del 20%");
            totalconsumo = totalconsumo * 1.20;
            System.out.println("El valor total a pagar de su factura es de: "+totalconsumo);
        }
    }
    
}
