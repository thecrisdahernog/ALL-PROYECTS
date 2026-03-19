/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package repaso1;

import java.util.Scanner;

/**
 *
 * @author Dell
 */
public class Repaso1 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        float Nota1, Nota2, Nota3, NotaFinal, promedio;
        System.out.println("Bienvenidos al Sistema de promedios de parciales");
        System.out.println("Procederemos a recibir las notas del estudiante");
        
        System.out.println("Ingrese la Nota del parcial #1: ");
        Nota1 = leer.nextFloat();
        
        System.out.println("Ingrese la Nota del parcial # 2: ");
        Nota2 = leer.nextFloat();
        
        System.out.println("Ingrese la Nota del parcial # 3:");
        Nota3 = leer.nextFloat();
        
        System.out.println("Ingrese la Nota del parcial Final: ");
        NotaFinal = leer.nextFloat();
        
        promedio = (Nota1 + Nota2 + Nota3 + NotaFinal)/4;
         
        if (promedio >= 3){            
            System.out.println("El Estudiante aprobo la materia con promedio" + promedio);
        }else{            
            System.out.println("El estudiante reprobo la materia con promedio" + promedio);
        }
        
        
    }
    
}
