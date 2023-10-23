#-----------------------------------------#
# Autor: Mizael S.                        #
# Fecha: 23/10/2023                       #
#-----------------------------------------#

# Guardamos la contraseña en una variable
password = "cadena"

# Iniciar un buble while para solicitar la contraseña al usuario hasta que sea correcta
while True:
    contraseña_ingresada = input("Ingrese la contraseña: ")
    if contraseña_ingresada == password:
        print("Contraseña correcta. Acceso concedido.")
        break  # Se sale del buble si la contraseña es correcta
    else:
        print("Contraseña incorrecta. Intente nuevamente.")