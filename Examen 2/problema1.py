#-----------------------------------------#
# Autor: Mizael S.                        #
# Fecha: 23/10/2023                       #
# Problema: 1                             #
#-----------------------------------------#

# Valores predeterminados
user = 'admin'
password = 'admin'
sesion_iniciada = False
trabajando = True

# Precios y cantidades iniciales
precios = {'diesel': 0, 'magna': 0, 'premium': 0}
cisterna = {'diesel': 0, 'magna': 0, 'premium': 0}
ventas_litros = {'diesel': 0, 'magna': 0, 'premium': 0}
ventas_pesos = {'diesel': 0, 'magna': 0, 'premium': 0}

while trabajando:
    # Verificar inicio de sesión
    if not sesion_iniciada:
        print("Bienvenido, por favor, inicia sesión")
        usuario = input("- Ingresa tu usuario: ")
        contraseña = input("- Ingresa tu contraseña: ")

        if usuario == user and contraseña == password:
            sesion_iniciada = True
            print("-------------------------------")
            print("- Contraseña correcta, se ha iniciado sesión")
        else:
            print("- Usuario o contraseña incorrectos. Inténtalo de nuevo.")
            continue
    # Mostrar el menu inicial
    print("-------------------------------")
    print("       MENU DE OPCIONES        ")
    print("1.- Apertura de caja")
    print("2.- Cierre de caja")
    print("3.- Salir del programa")
    opcion = input("- Selecciona una opción para continuar: ")
    # Iniciar con la lógica las opciones
    if opcion == '1':
        print("Apertura de caja...")
        # Establecer precios
        print("---------- ESTABLECER PRECIOS ----------")
        precios['diesel'] = float(input("- Establecer precio de Diesel: "))
        precios['magna'] = float(input("- Establecer precio de Magna: "))
        precios['premium'] = float(input("- Establecer precio de Premium: "))

        # Establecer litros iniciales
        print("----------- ESTABLECER LITROS -----------")
        cisterna['diesel'] = float(input("- Total de litros disponibles de Diesel: "))
        cisterna['magna'] = float(input("- Total de litros disponibles de Magna: "))
        cisterna['premium'] = float(input("- Total de litros disponibles de Premium: "))

        # Iniciar el bucle para las ventas
        while True:
            print("\nNueva carga de gasolina")
            tipo = input("Indique tipo de combustible (diesel/magna/premium): ").lower()
            if tipo in cisterna:
                litros = float(input("Indique el total de litros cargados: "))
                if litros <= cisterna[tipo]:
                    cisterna[tipo] -= litros
                    ventas_litros[tipo] += litros
                    total_pagar = litros * precios[tipo]
                    ventas_pesos[tipo] += total_pagar

                    # Mostrar ticket
                    print("\n----- TICKET DE PAGO -----")
                    print("Combustible:", tipo)
                    print("Litros:", litros)
                    print("Total: $", total_pagar)
                    print("¿Requiere factura?")
                    print("https://factura.lodemored.com/")
                    print("---------------------------")
                else:
                    print("No hay suficientes litros en la cisterna.")
            else:
                print("Tipo de combustible incorrecto.")

            # Preguntar si desea realizar otra carga
            continuar = input("¿Realizar otra carga? (s/n): ")
            if continuar.lower() != 's':
                break # romper el bucle
    
    # Logica para el cierre de caja
    elif opcion == '2':
        print("\nCierre de caja...")
        print("Resumen de ventas:")
        for combustible, litros in ventas_litros.items():
            print(f"{combustible.capitalize()}: {litros} litros - $ {ventas_pesos[combustible]}")
        print("Litros disponibles en cisterna:")
        for combustible, litros in cisterna.items():
            print(f"{combustible.capitalize()}: {litros} litros")
        sesion_iniciada = False  # Cerrar sesión para el siguiente usuario

    # Salir del programa si escoge 3 y mostrar mensaje de salida
    elif opcion == '3':
        print("Saliendo del programa. ¡Hasta luego!")
        trabajando = False
    else:
        print("Opción no válida. Intente de nuevo.")
