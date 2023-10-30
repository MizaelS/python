#-----------------------------------------#
# Autor: Mizael S.                        #
# Fecha: 30/10/2023                       #
# Clase 1 - Inputs, Variables y Prints    #
#-----------------------------------------#

# Solicitar datos al usuario
# Se utiliza la función input() para solicitar datos de tipo texto al usuario.
nombres = input("Ingrese sus nombres: ")
apellido_paterno = input("Ingrese su apellido paterno: ")
apellido_materno = input("Ingrese su apellido materno: ")

# Para solicitar datos numéricos, es necesario convertir el texto ingresado a un número.
# int(input()) convierte el texto ingresado a un número entero.
edad = int(input("Ingrese su edad: "))

# También es posible convertir el texto ingresado a un número de punto flotante con float(input()).
# Por ejemplo:
# estatura = float(input("Ingrese su estatura en metros: "))

# Mostrar datos en consola
# Se utiliza la función print() para mostrar texto en la consola.
print("╭────────────────────────────")

# Utilizando f-strings para incluir variables dentro de un texto.
# Las variables se colocan entre llaves {} y se muestran en el lugar correspondiente.
print(f"│ Su nombre es: {nombres}")
print(f"│ Su apellido paterno es: {apellido_paterno}")
print(f"│ Su apellido materno es: {apellido_materno}")
print(f"│ Su edad es: {edad}")
print("╰────────────────────────────")