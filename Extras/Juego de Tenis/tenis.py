import time
import os
import random

def actualiza(posicion_x, velocidad_x, posicion_y, velocidad_y, tiempo):
    resultado_x = posicion_x + velocidad_x * tiempo
    resultado_y = posicion_y + velocidad_y * tiempo
    return resultado_x, resultado_y

def mi_render(posicion_x, largo, posicion_y, alto):
    resultado = ""
    for indice_y in range(1, alto + 1):
        for indice_x in range(1, largo + 1):
            if indice_x == 1 or indice_x == largo:
                resultado += "|"
            elif round(indice_y) == round(posicion_y) and round(indice_x) == round(posicion_x):
                resultado += "0"
            else:
                resultado += " "
        resultado += "\n"
    return resultado

def cambiar_velocidad(velocidad):
    nueva_velocidad = random.randint(10, 10)
    return nueva_velocidad if random.choice([True, False]) else -nueva_velocidad

# Programa principal
print("=========================")
print("* Juego de tenis en 2D *")
print("=========================")
input("Presiona cualquier tecla para comenzar")

# Inicialización de variables
posicion_x = 1
velocidad_x = 10
largo = 10
posicion_y = 1
velocidad_y = 10
alto = 10
tiempo_final = 100
dt = 0.1

tiempo_inicial = 0
while tiempo_inicial < tiempo_final:
    nueva_posicion_x, nueva_posicion_y = actualiza(posicion_x, velocidad_x, posicion_y, velocidad_y, dt)

    if nueva_posicion_y <= 1:
        velocidad_y = abs(velocidad_y)
        nueva_posicion_y = 1
    elif nueva_posicion_y >= alto:
        velocidad_y = -abs(velocidad_y)
        nueva_posicion_y = alto

    if nueva_posicion_x <= 1:
        velocidad_x = abs(velocidad_x)
        nueva_posicion_x = 1
    elif nueva_posicion_x >= largo:
        velocidad_x = -abs(velocidad_x)
        nueva_posicion_x = largo

    posicion_x, posicion_y = nueva_posicion_x, nueva_posicion_y

    linea = mi_render(posicion_x, largo, posicion_y, alto)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(linea)
    print(f"Posición: {round(posicion_x)}, {round(posicion_y)}")

    time.sleep(0.2)
    tiempo_inicial += dt
