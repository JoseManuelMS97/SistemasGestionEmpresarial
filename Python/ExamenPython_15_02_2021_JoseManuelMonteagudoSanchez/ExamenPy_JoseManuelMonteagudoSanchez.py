import random

def GenerarCircuito(filas, columnas):
    circuito = []
    aux = "----"

    # Añade "----" a todas las posiciones
    for x in range(filas):
        list_aux = []
        for i in range(columnas):
            list_aux.append(aux)
        circuito.append(list_aux)

    # Añade a los coches en casillas aleatorias
    fila_aleatoria1=0
    fila_aleatoria2=0
    columna_aleatoria1=0
    columna_aleatoria2=0
    #Bucle hasta que se obtengan casillas distinas para los coches
    while((fila_aleatoria1==fila_aleatoria2) and (columna_aleatoria1==columna_aleatoria2)):
        fila_aleatoria1 = random.randint(0, filas - 1)
        columna_aleatoria1 = random.randint(0, columnas - 1)

        fila_aleatoria2 = random.randint(0, filas - 1)
        columna_aleatoria2 = random.randint(0, columnas - 1)

    #Se introducen los coches en esas casillas
    circuito[fila_aleatoria1][columna_aleatoria1] = f"Coche-1"
    circuito[fila_aleatoria2][columna_aleatoria2] = f"Coche-2"

    return circuito


def MostrarCircuito(matriz):
    for x in matriz:
        for i in x:
            print(i, end="\t")
        print()
    print()

def Choque(circuito,coches):
    #Creamos diccionario y hallamos las posiciones
    diccionario_coches = {'Coche-1':[0,0],
                          'Coche-2':[0,0]}

    for fila in range(len(circuito)):
        for columna in range(fila):
            if(circuito[fila][columna] == coches[0]):
                diccionario_coches[0][0] = fila
                diccionario_coches[0][1] = columna
                fila_aux1 = fila
                columna_aux1 = columna

            elif(circuito[fila][columna] == coches[1]):
                diccionario_coches[1][0] = fila
                diccionario_coches[1][1] = columna
                fila_aux2 = fila
                columna_aux2 = columna

    #Hallar que coche se mueve
    se_mueve = random.randint(0, 1)

    aux = "----"
    #Movemos el coche una fila abajo
    if(se_mueve==0):
        for fila_aux1 in range(len(circuito)-1):
            circuito[fila_aux1+1][columna_aux1] = "Coche-1"
            circuito[fila_aux1][columna_aux1] = aux


    if (se_mueve == 1):
        for fila_aux2 in range(len(circuito) - 1):
            circuito[fila_aux2 + 1][columna_aux1] = "Coche-2"
            circuito[fila_aux2][columna_aux2] = aux

    if ((fila_aux1==fila_aux2) and (columna_aux1 == columna_aux2)):
        print(f"Han chocado en: [{fila}, {columna}]")
    else:
        print("No hay choque")






filas = 0
columnas = 0
coches = ["Coche-1", "Coche-2"]

#Pedimos filas y columnas hasta que sean distintas, y mayor o igual que 4
while ((filas<4) or (columnas<4) or (filas==columnas)):
    filas = int(input("Indique el número de filas (mínimo 4): "))
    columnas = int(input("Indique el número de columnas (mínimo 4): "))


circuito = GenerarCircuito(filas,columnas)
MostrarCircuito(circuito)
Choque(circuito,coches)
