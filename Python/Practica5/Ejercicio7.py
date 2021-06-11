def myFunc(e):
    return len(e)


def cadena_mas_larga(list):
    resultado = []
    print("De la lista : ", cadena)
    cadena.sort(reverse=True, key=myFunc)

    mayor = len(cadena[0])
    contador = 0
    i = cadena[contador]

    while len(i) == mayor:
        resultado.append(i)
        contador += 1
        i = cadena[contador]

    print("La cadena o cadenas mas largas son: ", resultado)



cadena = ['Pepe', 'Ana', 'Juan', 'Paz']
cadena_mas_larga(cadena)
