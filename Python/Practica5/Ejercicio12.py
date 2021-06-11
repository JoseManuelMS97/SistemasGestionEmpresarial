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


print(f"Se ha generado la matriz: {generar_matriz()}")