# -----------------------------------------------------------------------------
# Autor: Mizael S.
# Fecha: 18/10/2023
# Descripción: Este script compara dos números, modifica uno de ellos y
#              realiza una nueva comparación. Imprime ciertos mensajes en
#              consola independientemente del resultado de las comparaciones.
# -----------------------------------------------------------------------------

# Declaración e inicialización de variables
numero1 = 5
numero2 = 1

# Primera comparación: Verifica si los números son iguales
if numero1 == numero2:
    print("Los números son iguales")

# Mensaje que se imprime siempre, independientemente del resultado de la comparación anterior
print("Este string se imprime siempre")

# Modificación del valor de la variable numero2
print("Ahora cambio el valor del número 2")
numero2 = 1

# Segunda comparación: Verifica nuevamente si los números son iguales
if numero1 == numero2:
    print("Los números son iguales")

# Mensaje que se imprime siempre, independientemente del resultado de la comparación anterior
print("Este string se imprime siempre")
