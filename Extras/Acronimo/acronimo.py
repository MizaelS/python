#-----------------------------------------#
# Nombre: Mizael S.                       #
# Fecha: 20/10/2023                       #
#           Generar Acronimos             #
#-----------------------------------------#

# Función para obtener el acronimo
def obtener_acronimo(frase):
    palabras = frase.split()  # Divide la frase en palabras
    acronimo = "".join([palabra[0].upper() for palabra in palabras if palabra])  # Toma la primera letra de cada palabra
    return acronimo

# Funcion principal
def main():
    print("Generador de Acronimos")
    print("-----------------------")
    while True:
        frase = input("Ingrese la frase (o 'salir' para terminar): ")
        if frase.lower() == 'salir': # Se usa "lower" para convertir el texto ingresado a minuscula
            break
        acronimo = obtener_acronimo(frase)
        print(f"Acrónimo: {acronimo}\n") # Impimir el acronimo obtenido

# Al ejecutarse el programa se llama a la función main
if __name__ == "__main__":
    main()
