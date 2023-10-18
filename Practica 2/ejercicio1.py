#-----------------------------------------#
# Autor: Mizael S.                        #
# Fecha: 18/10/2023                       #
#-----------------------------------------#

def es_divisible():
    """
    Esta función solicita al usuario que ingrese dos números enteros, N y M,
    y verifica si N es divisible por M, imprimiendo el resultado en consola.
    """
    
    # Solicita al usuario que ingrese el número N
    N = int(input("Ingresa el número N: "))
    
    # Solicita al usuario que ingrese el número M
    M = int(input("Ingresa el número M: "))

    # Verifica si N es divisible por M utilizando el operador módulo (%)
    if N % M == 0:
        # Imprime que N es divisible por M si no hay residuo
        print(f"{N} es divisible por {M}")
    else:
        # Imprime que N no es divisible por M si hay un residuo
        print(f"{N} no es divisible por {M}")

# Invoca a la función es_divisible para ejecutar la lógica
es_divisible()
