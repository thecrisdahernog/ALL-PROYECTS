/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.areacirculo;

import java.util.Scanner;


/**
 *
 * @author Dell
 */
public class AreaCirculo {

    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        double radio;        
        double area;
        System.out.println("Ingrese el radio");
        radio = leer.nextDouble();
        area = Math.PI * Math.pow(radio,2);        
        System.out.println("El area del circulo es: "+ area);
    }
}
