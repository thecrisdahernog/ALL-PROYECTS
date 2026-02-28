/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.agricultores;

import java.util.Scanner;

/**
 *
 * @author Dell
 */
public class Agricultores {

    public static void main(String[] args) {
        Scanner leer = new Scanner (System.in);
        double KiloUva,cantidad,precio,total;
        int Tipo,Tamaño;
        
        System.out.println("Bienvenidos al sistema de revision de pedidos de uva");
        System.out.println("Ingrese el precio del Kilo de Uva");
        KiloUva = leer.nextDouble();
        System.out.println("debe ingresar primero el tipo de uva que desea");
        System.out.println("Elija 1. Tipo A \n 2. Tipo B");
        Tipo = leer.nextInt();
        System.out.println("Ademas debe elegir tambien el tamano de la uva");
        System.out.println("elija 1. Tamano 1 \n2.Tamano 2");
        Tamaño = leer.nextInt();
        if (Tipo == 1){
            if (Tamaño == 1){
            KiloUva = KiloUva + 0.20;}
            else if (Tamaño == 2){
            KiloUva = KiloUva + 0.30;}
        }else if(Tipo == 2){
            if (Tamaño == 1){
            KiloUva = KiloUva -0.30;}
            else if (Tamaño == 2){
            KiloUva = KiloUva - 0.50;
            }
        }
        System.out.println("Ingrese la Cantidad a llevar de uvas: ");
        cantidad = leer.nextDouble();
        total = KiloUva * cantidad;
        System.out.println("Las uvas de tipo "+ Tipo +" y de tamano " + Tamaño + " tienen un valor de " + KiloUva);
        System.out.println("El total de su compra es de: " + total );
    }
}
