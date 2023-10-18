#-----------------------------------------#
# Nombre: Mizael S.                       #
# Fecha: 16/10/2023                       #
#-----------------------------------------#

def evaluar_caracter(caracter):
    # Convertir el carácter a minúscula para uniformidad y evitar falsos negativos
    caracter = caracter.lower()

    # Lissta de vocales
    vocales = ['a', 'e', 'i', 'o', 'u']

    # Verificar si el carácter es una vocal
    if caracter in vocales:
        return "✅ Verdadero, el carácter es una vocal."
    # Si el carácter es alfabético y no es una vocal, entonces es una consonante
    elif caracter.isalpha():
        return "❌ El carácter es una consonante."
    # Si el carácter es alfanumérico, verificar si es un número
    elif caracter.isdigit():
        return "❌ El carácter es un número."
    # Si el carácter no es alfabético ni numérico, entonces es un signo
    else:
        return "❌ El carácter es un signo."
      
# Solicitar al usuario que ingrese un carácter
caracter = input("- Introduce el carácter a evaluar: ")

# Pasar el carácter a la función y obtener el resultado
resultado = evaluar_caracter(caracter)

# Imprimir resultados
print(f"{resultado}")