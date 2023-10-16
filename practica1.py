#-----------------------------------------#
# Nombre: Mizael S.                       #
# Fecha: 16/10/2023                       #
#-----------------------------------------#

def evaluar_caracter(caracter):
    # Convertidos el caracter a minuscula para evitar falsos
    caracter = caracter.lower()
    # Lissta de vocales
    vocales = ['a', 'e', 'i', 'o', 'u']

    # Verificamos si el caracter es una vocal
    if caracter in vocales:
        return "✅ Verdadero, el caracter es una vocal."
    # Se verifica si el caracter es alfabetico y no es una vocal entonces es una consonante
    elif caracter.isalpha():
        return "❌ El caracter es una consonante."
    # Se verifca si el caracter es una un número
    elif caracter.isalnum():
        return "❌ El caracter es un número."
    # Si no es alfabecito entonces es un signo
    else:
        return "❌ El caracter es un signo."
      
# Obtener el caracter que ingrese el usuario 
caracter = input("- Introduce el caracter a evaluar: ")

# Pasar los datos a la función
resultado = evaluar_caracter(caracter)

# Imprimir resultados
print(f"{resultado}")