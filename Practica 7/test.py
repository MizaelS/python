#-----------------------------------------#
# Nombre: Mizael S.                       #
# Fecha: 22/11/2023                       #
#-----------------------------------------#

archivo = open("config.txt", "r+")
# archivo.write("Hola mundo")

texto = archivo.read()

print(texto)

archivo.close()