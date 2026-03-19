/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package repasodificil3;

import java.util.Scanner;
/**
 *
 * @author Dell
 */
public class Repasodificil3 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        double peso,altura,imc,redondeo;
        String nombre;
        System.out.println("Bienvenido al calculador de IMC");
        System.out.println("Ingrese por favor su nombre");
        nombre = leer.next();
        System.out.println("Ingrese por favor su peso en kilogramos");
        peso = leer.nextDouble();
        System.out.println("Ingrese por favor su altura en metros");
        altura = leer.nextDouble();
        imc = peso / Math.pow(altura, 2);
        redondeo = Math.round(imc*100)/100.0;
        if (imc >= 30){
            System.out.println(nombre+" Su IMC es: "+redondeo+" ,Usted tiene obesidad.");
        }else if (imc >= 25){
            System.out.println(nombre+" Su IMC es: "+redondeo+" Usted tiene sobrepeso");
        }else if (imc >= 18.5){
            System.out.println(nombre+" Su IMC es: "+redondeo+" Usted esta dentro de los Rangos normales");
        }else {
            System.out.println(nombre+" Su Imc es: "+redondeo+" Usted se encuentra Bajo de peso");
        }
    leer.close();
    }
    
}
