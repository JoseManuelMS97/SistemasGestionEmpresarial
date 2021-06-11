import random


def generar_circuito(nombres, longitud):
    matriz = ""

    for filas in range(len(nombres)):

        for columnas in range(longitud):

            if columnas == 0:
                matriz += f"\t{nombres[filas]}\t"

            else:
                matriz += "\t----\t"

        matriz += "\n"

    return matriz


def mostrar_circuito(matriz):
    print(matriz)


def carrera(matriz, nombres, longitud):
    puntos = [0] * len(nombres)
    meta = longitud
    ganador = list()

    while ganador == list():

        aleatorio = random.randint(0, len(nombres) - 1)

        for numero in range(len(nombres)):

            if aleatorio == numero:
                puntos[numero] += 3

            else:
                puntos[numero] += 1

            if puntos[numero] >= meta:
                puntos[numero] = longitud - 1
                ganador.append(nombres[numero])

        matriz = ""

        for filas in range(len(nombres)):

            for columnas in range(longitud):

                if columnas == puntos[filas]:
                    matriz += f"\t{nombres[filas]}\t"

                else:
                    matriz += "\t----\t"

            matriz += "\n"

        print(matriz)

    print(f"Ganador: {ganador}" )


nombres_introducidos = list()
participantes = int(input("Introduce el número de participantes: "))

for i in range(participantes):
    nombres_introducidos.append(input(f"Indica el nombre del participante {i + 1}: "))

longitud_introducida = int(input("Indique la longitud del circuito (mínimo 6): "))

cadena = generar_circuito(nombres_introducidos, longitud_introducida)
mostrar_circuito(cadena)
carrera(cadena, nombres_introducidos, longitud_introducida)
