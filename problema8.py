#-----------------------------------------#
# Nombre: Mizael S.                       #
# Fecha: 03/10/2023                       #
#-----------------------------------------#

# Definir la función para calcular el tiempo de encuentro
def tiempo_encuentro(v1, v2, distancia):
    return distancia / (v1 + v2)

# Obtener los datos necesarios para evaluar la formaula
v1 = float(input("- Introduce la velocidad del primer cuerpo: "))
v2 = float(input("- Introduce la velocidad del segundo cuerpo: "))
distancia = float(input("- Introduce la distancia inicial que los separa: "))

# Llamar a la función con los datos recolectados
t = tiempo_encuentro(v1, v2, distancia)

# Imprimir resultados
print(f"- El tiempo de encuentro es: {t} unidades de tiempo")