matriz = []
fila = []

for i in range(1, 6):
    fila = input(f"Introduzca fila {i}: ")
    matriz.append(list(map(int, fila.split())))

sum_colums = []
sum_filas = []
aux_colums = 0
aux_filas = 0

for f in range(len(matriz)):
    for c in range(len(matriz)):
        aux_colums += matriz[c][f]
        aux_filas += matriz[f][c]
    sum_filas.append(aux_filas)
    sum_colums.append(aux_colums)
    aux_colums = 0
    aux_filas = 0

print(f"\nTotales filas: {sum_filas}")
print(f"Totales columnas: {sum_colums}")