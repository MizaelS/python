#-----------------------------------------#
# Autor: Mizael S.                        #
# Fecha: 23/10/2023                       #
#-----------------------------------------#

# Pedir al usuario la altura del triangulo
altura = int(input("Introduce la altura del triángulo: "))

# Iniciar el bucle for iterarando desde 1 hasta el número ingresado
for i in range(1, altura + 1):
    # Imprimir una línea de * de longitud i
    print('*' * i)