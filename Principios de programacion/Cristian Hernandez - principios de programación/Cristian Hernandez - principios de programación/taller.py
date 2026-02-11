Nombre = "Cristian Hernandez"
Nombre = input("ingrese su nombre completo")
Asunto = "Informe sobre notas de seguimiento"
Informacion = "estimado Sr por medio del presente correo le informamos el numero de notas, su nota definitiva y si aprobo o no el curso"
Correo = "crhis-123@hotmail.com"
N1 = float(input("ingrese la nota 1: "))
N2 = float(input("ingrese la nota 2: "))
N3 = float(input("ingrese la nota 3: "))
Nf = N1 + N2 + N3
NF1 = Nf/3
ResultadoFinal = "el Estudiante aprobo la materia"
footer = "Agradecemos de antemano la atencion prestada"
Mensaje = "te invitamos a seguir con tu proceso de educacion"
Final = "Jhonny Duarte"
print(f"{Nombre} \n {Asunto} \n {Informacion} \n {Correo} \n sus notas finales son: \n Nota 1 = {N1} \n Nota 2 = {N2} \n Nota 3 = {N3} \n Nota Definitiva = {NF1} \n {ResultadoFinal} \n {footer} \n {Mensaje} \n {Final} " )