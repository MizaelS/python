#-----------------------------------------#
# Autor: Mizael S.                        #
# Fecha: 23/10/2023                       #
#-----------------------------------------#

# Solicitamos el número a evaular al usuario
numero = int(input("Ingrese el número: "))

# Creamos el bucle for para iterar en los numeros impares del numero ingresado
for i in range(1, numero + 1, 2):
    # Imprimimos los resultados desde el 1 hasta el final
    print(i, end=",")