matriz = [] 

for i in range(3): 
    fila = [] 
    for dato in range(3): 
        valor = int(input(f"Ingrese el valor: "))
        fila.append(valor)

    matriz.append(fila)  

print("Matriz ingresada:")
for fila in matriz:
    print(fila)
