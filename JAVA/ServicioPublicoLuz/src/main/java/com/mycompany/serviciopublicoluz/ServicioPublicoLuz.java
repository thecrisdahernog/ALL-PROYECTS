/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 */

package com.mycompany.serviciopublicoluz;

import java.util.Scanner;

/**
 *
 * @author Dell
 */
public class ServicioPublicoLuz {

    public static void main(String[] args) {
        Scanner leer = new Scanner(System.in);
        double consumo, subtotal, total, valorKw = 863;
        int tipoInmueble, estrato;
        
        System.out.println("Ingrese el consumo");
        consumo = leer.nextDouble();
        System.out.println("Ingrese tipo de inmueble");
        System.out.println("1. Residencia\n2. Comercio");
        tipoInmueble = leer.nextInt();
        System.out.println("Ingrese el estrato");
        estrato = leer.nextInt();
        
        if(tipoInmueble == 1){
            subtotal = consumo*valorKw;
            if(estrato<=3){
                total = subtotal - (subtotal*0.20);
            }else{
                total = subtotal;
            }
        }else{
            subtotal = (consumo*80)*valorKw;
            if(estrato<=3){
                total = subtotal - (subtotal*0.20);
            }else{
                total = subtotal;
            }
        
        }       
        
        System.out.println("Total a pagar $" + total);
    }        
}
