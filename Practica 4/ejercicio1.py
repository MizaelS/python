#-----------------------------------------#
# Autor: Mizael S.                        #
# Fecha: 06/11/2023                       #
#-----------------------------------------#

arreglo = []

print("- Ingrese el numero que agregarás o ingresa 'x' para terminar: ")
while True:
    nuevo_dato = input()
    if nuevo_dato.lower() == 'x':
        break
    arreglo.append(int(nuevo_dato))

print("Arreglo original:", arreglo)

lista_posiciones_impares = [numero for indice, numero in enumerate(arreglo) if indice % 2 != 0]
lista_posiciones_pares = [numero for indice, numero in enumerate(arreglo) if indice % 2 == 0]

print("Elementos en posiciones impares:", lista_posiciones_impares)
print("Elementos en posiciones paer:", lista_posiciones_pares)


# datos = []

# while True:
#     dato = input()
#     if dato.lower() == 'x':
#         break
#     datos.append(int(dato))

# for x in range(len(datos)):
#     if x % 2 == 0:
#         datos.pop(x)
#         print(datos)    
