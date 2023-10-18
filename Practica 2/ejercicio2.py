#-----------------------------------------#
# Autor: Mizael S.                        #
# Fecha: 18/10/2023                       #
#-----------------------------------------#

def convertir_temperatura():
    """
    Esta función solicita al usuario que ingrese una temperatura y su unidad
    (Celsius o Fahrenheit), y realiza la conversión correspondiente, imprimiendo
    el resultado en consola.
    """

    # Solicita al usuario que ingrese la temperatura
    temperatura = float(input("Ingresa la temperatura: "))

    # Solicita al usuario que ingrese la unidad de la temperatura (Celsius o Fahrenheit)
    unidad = input("¿En qué unidad está la temperatura (Celsius/Fahrenheit)? Ingresa C o F: ")

    # Convierte la unidad a mayúsculas para asegurar consistencia en la comparación
    unidad = unidad.upper()

    if unidad == 'C':
        # Convierte la temperatura de Celsius a Fahrenheit usando la fórmula: F = (C * 9/5) + 32
        convertida = (temperatura * 9/5) + 32
        print(f"{temperatura} grados Celsius equivalen a {convertida} grados Fahrenheit")
    elif unidad == 'F':
        # Convierte la temperatura de Fahrenheit a Celsius usando la fórmula: C = (F - 32) * 5/9
        convertida = (temperatura - 32) * 5/9
        print(f"{temperatura} grados Fahrenheit equivalen a {convertida} grados Celsius")
    else:
        # Notifica al usuario si la unidad ingresada no es reconocida
        print("Unidad no reconocida. Por favor, ingresa C o F.")

# Invoca a la función convertir_temperatura para ejecutar la lógica
convertir_temperatura()
