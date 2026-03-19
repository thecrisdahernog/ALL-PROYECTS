/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package repaso3;

import java.util.Scanner;

/**
 *
 * @author Dell
 */
public class Repaso3 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        double area,radio;
        System.out.println("vamos a sacar el area de un circulo.");
        System.out.println("para eso, por favor ingrese el radio del circulo, para iniciar el calculo.");
        radio = leer.nextDouble();
        area = (Math.PI)*(Math.pow(radio, 2));
        if (area >= 100){
            System.out.println("El area de su circulo es: "+area);
            System.out.println("El circulo segun sus datos es Grande");
        }else{
            System.out.println("El area de su circulo es: "+area);
        }
    }
    
}
