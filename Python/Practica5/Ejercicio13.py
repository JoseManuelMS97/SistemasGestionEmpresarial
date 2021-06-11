import random


def generar_matriz():
    num_filas = random.randint(2, 6)
    num_columnas = random.randint(2, 6)

    matriz = [None] * num_columnas

    for i in range(len(matriz)):
        matriz[i] = [None] * num_filas
        for j in range(len(matriz[i])):
            rand = random.randint(0, 100)
            matriz[i][j] = rand
    return matriz


matriz = generar_matriz()

if len(matriz) == len(matriz[0]):
    suma = 0
    for i in range(len(matriz)):
        print(matriz[i][i])
        suma += matriz[i][i]
else:
    print(f"La matriz no es cuadrada! ({len(matriz)} X {len(matriz[0])})")
