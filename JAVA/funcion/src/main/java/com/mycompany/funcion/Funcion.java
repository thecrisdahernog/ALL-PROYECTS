/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.funcion;

import java.util.Scanner;

/**
 *
 * @author Dell
 */
public class Funcion {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Ingrese el valor de a: ");
        double a = scanner.nextDouble();
        System.out.println("Ingrese el valor de b: ");
        double b = scanner.nextDouble();
        System.out.println("Ingrese el valor de c:");
        double c = scanner.nextDouble();
        double x = (-b+ (Math.sqrt(Math.pow(b,2)-(4*a*c))))/(2*a);
        System.out.println("El resultado de la operacion es: "+ x);
    }
}
