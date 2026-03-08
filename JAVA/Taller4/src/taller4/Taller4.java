/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package taller4;

import java.util.Scanner;

/**
 *
 * @author Dell
 */
public class Taller4 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        double radio,volumen;
        System.out.println("Iniciamos el programa para calcular el volumen de una esfera");
        System.out.println("Ingrese por favor el radio de la esfera");
        radio = leer.nextDouble();
        volumen = (4/3)*Math.PI*Math.pow(radio, 3);
        if (volumen > 500){
            System.out.println("El volumen de esta esfera supera las 500 unidades cubicas");
        }else{
            System.out.println("El volumen de esta esfera no supera las 500 unidades cubicas");
        }
    }
    
}
