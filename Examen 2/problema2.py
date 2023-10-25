#-----------------------------------------#
# Autor: Mizael S.                        #
# Fecha: 23/10/2023                       #
# Problema: 2                             #
#-----------------------------------------#

# Definimos N y M
N = int(input("Por favor, ingrese el número entero N: "))
M = int(input("Por favor, ingrese el número entero M: "))

# Verificamos si son enteros positivos
if N <= 0 or M <= 0:
    print("Por favor, ingrese números enteros positivos.")
else:
    # Inicia la logica para la creación de la tabla
    # Ponemos de cabezera a M
    print(f'{"":>3}', end='')

    # Imprimimos los números del 1 al M
    for i in range(1, M + 1):
        print(f'{i:>4}', end='')

    # Ponemos una linea de división
    print("\n" + "-" * (4 * M + 3))

    # Ponemos las filas en la tabla de multiplicar
    for i in range(1, N + 1):
        # Imprimimos el primer número
        print(f'{i:>3}|', end='')

        # Calculamos e imprimimos cada entrada en la fila
        for j in range(1, M + 1):
            print(f'{i * j:>4}', end='')

        # Pasamos a la siguiente línea en la tabla
        print()