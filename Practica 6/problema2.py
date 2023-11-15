#-----------------------------------------#
# Nombre: Mizael S.                       #
# Fecha: 15/11/2023                       #
#-----------------------------------------#

import random

# Vectores
vector1 = [random.randint(1, 100) for _ in range(5)]
vector2 = [random.randint(1, 100) for _ in range(5)]

vector3_suma = [a + b for a, b in zip(vector1, vector2)]
vector3_resta = [a - b for a, b in zip(vector1, vector2)]
vector3_multiplicacion = [a * b for a, b in zip(vector1, vector2)]
vector3_division = [a / b if b != 0 else None for a, b in zip(vector1, vector2)]

print("Vector 1:", vector1)
print("Vector 2:", vector2)
print("Suma (Vector 1 + Vector 2):", vector3_suma)
print("Resta (Vector 1 - Vector 2):", vector3_resta)
print("Multiplicación (Vector 1 * Vector 2):", vector3_multiplicacion)
print("División (Vector 1 / Vector 2):", vector3_division)