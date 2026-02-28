/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.hipotenusatriangulo;

import java.util.Scanner;

/**
 *
 * @author Dell
 */
public class HipotenusaTriangulo {

    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        System.out.println("Ingrese el valor del primer lado: ");
        double a = leer.nextDouble();
        System.out.println("Ingrese el valor del segundo lado: ");
        double b = leer.nextDouble();        
        double c = (Math.pow(a, 2))+ Math.pow(b, 2);
        c = Math.sqrt(c);
        System.out.println("La hipotenusa del trinagulo es: "+ c);
        
        
    }
}
