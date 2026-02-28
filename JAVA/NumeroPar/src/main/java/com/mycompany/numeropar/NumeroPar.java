/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.numeropar;

import java.util.Scanner;

/**
 *
 * @author Dell
 */
public class NumeroPar {

    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        int numero;
        System.out.println("Ingrese un numero");
        numero = leer.nextInt();
                
        if((numero%2) == 0){
            System.out.println("El numero es par");
        }else{
            System.out.println("El numero es impar");
        }
    }
}
