#-----------------------------------------#
# Nombre: Mizael S.                       #
# Fecha: 20/10/2023                       #
#        Calculador de propinas           #
#-----------------------------------------#

# Mensaje de bienvenida y recolección de datos
subtotal = float(input("Bienvenido, por favor, ingrese el monto de la factura total: "))

# Pedir al usuario que % de propina quiere dejar
porcentaje_propina = float(input(f"Ingrese el % de propina que desea dejar para el total de ${subtotal}: "))

# Calcular el total de propina en base al porcentaje que ingreso el usuario
propina = subtotal * (porcentaje_propina / 100)

# Calcular el total de la cuenta (subtotal + propina)
total = propina + subtotal

# Imprimir el total de la propina y adjuntar el costo total
print(f"La propina aplicando {porcentaje_propina}% es de ${propina}, el total a pagar es de ${total}.")