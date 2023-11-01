# Solicitamos datos al usuario
nombre = input("Ingrese su nombre: ")
peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

# Calculamos el IMC
# Formula: IMC = peso / altura^2
imc = peso / (altura ** 2)

# Redondeamos el IMC a dos decimales
imc = round(imc, 2)

# Mostramos los datos y el IMC en la consola
print("╭────────────────────────────")
print(f"│ Nombre: {nombre}")
print(f"│ Peso: {peso} kg")
print(f"│ Altura: {altura} m")
print(f"│ IMC: {imc}")
print("╰────────────────────────────")
