#-----------------------------------------#
# Nombre: Mizael S.                       #
# Fecha: 15/11/2023                       #
#-----------------------------------------#

n = int(input("Ingrese el número de equipos, el valor debe ser menor que 10: "))

if n >= 10:
    print("El número de equipo debe ser menor que 10")
else:
    m_matriz = []

    for i in range(n):
        resultados_equipos = []
        for j in range(n):
            if i == j:
                resultados_equipos.append(0)
            else:
                gol = int(input(f"Ingrese los goles que marco el equipo {i+1} y {j+1}: "))   
                resultados_equipos.append(gol)
                m_matriz.append(resultados_equipos)

    puntos = [0 for _ in range(n)]            

    for i in range(n):
        for j in range(n):
            if i != j:
                if m_matriz[i][j] > m_matriz[j][i]:
                    puntos[i] += 3 # Ganan
                elif m_matriz[i][j] == m_matriz[j][i]:
                    puntos[i] += 1 # Empate

    for i, p in enumerate(puntos):
        print(f"Equipo {i+1}: {p} puntos")                

