import math


def es_repeticion(cadena):
    mitad = (math.floor(len(cadena) / 2))

    primera_mitad = cadena[:mitad]
    segunda_mitad = cadena[mitad:]

    if (primera_mitad == segunda_mitad):
        return True
    else:
        return False


cadena = input("Introduzca una cadena: ")
if(es_repeticion(cadena)):
    print("La cadena SI esta formada por la concatenacion de otra cadena igual a ella. ")
else:
    print("La cadena NO esta formada por la concatenacion de otra cadena igual a ella. ")

