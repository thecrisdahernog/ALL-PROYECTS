/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package repasodificil1;

import java.util.Scanner;

/**
 *
 * @author Dell
 */
public class Repasodificil1 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        double Peso,Distancia,Costo,redondeo;
        int Tipo;
        System.out.println("Bienvenidos al sistema de calculo de envios internacionales");
        System.out.println("Ingrese por favor el Peso de su paquete en kilogramos");
        Peso = leer.nextFloat();
        System.out.println("Ingrese por favor la distancia que va a recorrer el paquete en kilometros");
        Distancia = leer.nextFloat();
        System.out.println("Elija por favor el tipo de envio:\n1.Normal.\n2.Express.");
        Tipo = leer.nextInt();
        
        if (Tipo==1){
            Costo = (Peso * 5)+(Distancia *0.02);
            System.out.println("El total del costo de su envio es: "+Costo); 
        }else if (Tipo == 2){
            Costo = ((Peso * 5)+(Distancia *0.02))*1.35;
            redondeo = Math.round(Costo*100)/100.0;
            System.out.println("El total del costo de su envio es: "+redondeo); 
        }
          
    }
    
}
