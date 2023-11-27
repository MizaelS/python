#-----------------------------------------#
# Nombre: Mizael S.                       #
# Fecha: 22/11/2023                       #
#-----------------------------------------#

# Declaramos el nombre del archivo como varaible
texto = "texto.txt"

# Abrimos el archivo usando la variable
with open(texto, "r", encoding="UTF-8") as archivo:
    lineas = archivo.readlines()

for num_linea, linea in enumerate(lineas, start=1):
    linea_limpia = linea.rstrip('.\n').replace(' ', '').lower()
    linea_limpia = "".join(c for c in linea if c.isalnum()).lower()

    if linea_limpia == linea_limpia[::-1]:
        print(f"La linea {num_linea} es palindroma: {linea}")