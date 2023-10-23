#-----------------------------------------#
# Autor: Mizael S.                        #
# Fecha: 23/10/2023                       #
#-----------------------------------------#

# Pedir al usuario la cantidad a invertir
inversion = float(input("Ingrese la cantidad a invertir: "))

# Pedir al usuario el interés anual
interes = float(input("Ingrese el interés anual: "))

# Pedir al usuario el número de años de la inversión
tiempo = int(input("Ingrese el número de años: "))

# Iniciar con el bucle for
for i in range(1, tiempo + 1):
    # Calcular el capital obtenido utilizando la fórmula de interés compuesto
    capital_obtenido = inversion * (1 + interes/100)**i

    # Redondear el resultado a 2 decimales
    capital_obtenido = round(capital_obtenido, 2)  

    # Imprimir el resultado mostrando el número de años (i) y el capital obtenido
    print(f"La capital obtenida tras {i} años es de {capital_obtenido}")