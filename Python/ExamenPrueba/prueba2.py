
matriz = [[1,2,3,4,5],
          [6,7,8,9,10],
          [11,12,13,14,15],
          [16,17,18,19,20],
          [21,22,23,24,25]]

#Imprimirla
for i in matriz:
    for j in i:
        print(j, end=" ")
    print()

#Pedir por filas
matriz2 = []
fila = []
for i in range(1, 6):
    fila = input(f"Introduzca fila {i}: ")
    matriz2.append(list(map(int, fila.split())))

#Suma de columnas y de filas
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