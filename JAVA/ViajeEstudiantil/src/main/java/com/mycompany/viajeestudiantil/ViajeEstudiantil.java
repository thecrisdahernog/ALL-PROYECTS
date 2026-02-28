/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.viajeestudiantil;

import java.util.Scanner;

/**
 *
 * @author Dell
 */
public class ViajeEstudiantil {

    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        //iniciamos ingresando las variables y su respectivo tipo
        int CantidadAlumnos;
        double Costo,Renta;
        System.out.println("Bienvenido a la agencia de viajes VOY Y VENGO");
        System.out.println("Para poder determinar el precio de su viaje, ingrese por favor la cantidad de pasajeros");
        CantidadAlumnos = leer.nextInt();
        if (CantidadAlumnos >= 100){
            Costo = 65;
            Renta = Costo * CantidadAlumnos;            
        }else if (CantidadAlumnos >= 50){
            Costo = 70;
            Renta = Costo * CantidadAlumnos; 
        }else if (CantidadAlumnos >= 30){
            Costo = 95;
            Renta = Costo * CantidadAlumnos; 
        }else{
            Renta = 4000;
            Costo = Renta / CantidadAlumnos;
        }
        System.out.println("la Cantidad de alumnos es: "+ CantidadAlumnos +" ,por lo tanto el precio por cada uno es: " + Costo);
        System.out.println("El valor total de su viaje es: "+Renta);
    }
}
