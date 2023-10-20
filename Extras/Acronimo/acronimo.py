#-----------------------------------------#
# Nombre: Mizael S.                       #
# Fecha: 20/10/2023                       #
#           Generar Acronimos             #
#-----------------------------------------#

# Función para obtener el acronimo
def obtener_acronimo(frase):
    palabras = frase.split() # Divide la frase en palabras
    acronimo = "".join([palabra[0].upper() for palabra in palabras if palabra])  # Toma la primera letra de cada palabra
    return acronimo # Se devuelve el acronimo generado

# Funcion principal
def main():
    print("Generador de Acronimos")
    print("-----------------------")
    while True: # Iniciar el bucle
        frase = input("Ingrese la frase (o 'salir' para terminar): ") # Imprimir el mensaje de bienvenida y obtener la frase para sacar el acronimo
        if frase.lower() == 'salir': # Se usa "lower" para convertir el texto ingresado a minuscula
            break # En caso de escribir "salir" se rompe el bucle y se sale del programa
        acronimo = obtener_acronimo(frase) # Llamar a la función obtener_acronimo con el dato frase obtenido del usuario
        print(f"Acrónimo: {acronimo}\n") # Impimir el acronimo obtenido

# Al ejecutarse el programa se llama a la función main
if __name__ == "__main__":
    main()
