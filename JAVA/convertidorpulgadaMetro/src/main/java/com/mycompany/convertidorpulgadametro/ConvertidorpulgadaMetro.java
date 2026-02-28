/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.convertidorpulgadametro;

import java.util.Scanner;

/**
 *
 * @author Dell
 */
public class ConvertidorpulgadaMetro {

    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        double pulgadas;
        double resultado;
        System.out.println("Ingrese la cantidad de pulgadas de tela que necesita el modista: ");
        pulgadas = leer.nextDouble();
        resultado = pulgadas * 0.0254;
        System.out.println("El total de metros de telas que pidio el cliente es: "+ resultado);
    }
}
