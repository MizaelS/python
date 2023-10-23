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
    capital_obtenido = inversion * (1 + interes/100)**i
    capital_obtenido = round(capital_obtenido, 2) # Redondemoa el resultado a 2 decimales
    print(f"La capital obtenida tras {i} es de {capital_obtenido} ") # Imprimir el resultado