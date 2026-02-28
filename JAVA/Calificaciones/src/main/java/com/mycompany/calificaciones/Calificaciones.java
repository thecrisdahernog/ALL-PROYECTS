/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.calificaciones;

import java.util.Scanner;

/**
 *
 * @author Dell
 */
public class Calificaciones {

    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        int nota;
        System.out.println("Ingrese el Valor de la nota");
        nota = leer.nextInt();
        
        if(nota >= 90){
            System.out.println("Excelente");
        } else if (nota < 90 && nota >= 80){
        System.out.println("Sobresaliente");}
       else if (nota < 80 && nota >= 70){
        System.out.println("aceptable");
    }   else if(nota < 70 && nota >= 30){
            System.out.println("Insuficiente");
    }else{
            System.out.println("Deficiente");
    }
    }
}
