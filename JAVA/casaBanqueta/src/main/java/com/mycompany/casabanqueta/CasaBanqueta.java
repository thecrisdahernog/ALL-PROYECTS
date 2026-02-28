package com.mycompany.casabanqueta;
import java.util.Scanner;
public class CasaBanqueta {
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        int NumeroAsistentes,membresia;
        double total;
        System.out.println("Ingrese el numero de asistentes al evento");
        NumeroAsistentes = leer.nextInt();
        System.out.println("Ingrese si tiene una membresia");
        System.out.println("1.Tiene Membresia\n2.No tiene membresia");
        membresia = leer.nextInt();        
        if(NumeroAsistentes >= 200){
            total = NumeroAsistentes * 50;
            System.out.println("El valor por asistente es de $50");            
        }else if(NumeroAsistentes >= 150){
            total = NumeroAsistentes * 70;
            System.out.println("El valor por asistente es de $70");            
        }else if(NumeroAsistentes >= 100){
            total = NumeroAsistentes * 90;
            System.out.println("El valor por asistente es de $90");            
        }else {
            total = NumeroAsistentes *150;
            System.out.println("El valor por asistente es de $150");
        }
        if (membresia == 1){
            total = total * 0.80;
            System.out.println("El total a pagar es de: $"+total);
        }else{
            System.out.println("El total a pagar es de: $"+total);
                    }
    }
}
