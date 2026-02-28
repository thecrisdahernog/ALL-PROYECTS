/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.sistemadepago;

import java.util.Scanner;

/**
 *
 * @author Dell
 */
public class SistemaDePago {

    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        int pago;
        double total;
        System.out.println("Ingrese el valor del articulo: ");
        pago = leer.nextInt();
        total = (pago * 0.8)*1.15;
        System.out.println("El total a pagar del cliente es: "+ total);
    }
}
