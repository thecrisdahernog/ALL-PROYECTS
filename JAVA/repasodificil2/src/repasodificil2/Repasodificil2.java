/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package repasodificil2;

import java.util.Scanner;
/**
 *
 * @author Dell
 */
public class Repasodificil2 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        double numero1,numero2,numero3,area,perimetro,s,radicando;
        System.out.println("Bienvenido al sistema para revisar si se puede formar un triangulo, por medio de 3 numeros reales");
        System.out.println("Ingrese por favor el primer numero");
        numero1 = leer.nextDouble();
        System.out.println("Ingrese por favor el Segundo numero");
        numero2 = leer.nextDouble();
        System.out.println("Ingrese por favor el tercer numero");
        numero3 = leer.nextDouble();
        if (((numero1+numero2)>numero3)&&((numero1+numero3)>numero2)&&((numero2+numero3)>numero1)){
            System.out.println("Se cumple la primera condicion de nuestra operacion: que el triangulo sea valido");
            System.out.println("procedemos ahora a determinar el semiperimetro");
            s = (numero1+numero2+numero3)/2;
            System.out.println("el semiperimetro es: "+s);
            radicando = s*(s-numero1)*(s-numero2)*(s-numero3);
            area = Math.sqrt(radicando);
            System.out.println("El area de este triangulo es: "+area);
            perimetro = numero1+numero2+numero3;
            System.out.println("El perimetro de este triangulo es: "+perimetro);
        }else{
            System.out.println("No se cumple la condicion de que el triangulo sea valido, debe probar con otras 3 numeros");
        }
        leer.close();
    }
    
}
