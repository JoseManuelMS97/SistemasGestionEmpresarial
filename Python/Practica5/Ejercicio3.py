dni = input("Introduzca su dni: ")

def es_nif(dni):
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"
    numeros = "1234567890"
    dni = dni.upper()
    if len(dni) == 9:
        letra = dni[8]
        dni = dni[:8]
        return len(dni) == len([n for n in dni if n in numeros]) \
               and letras[int(dni) % 23] == letra
    return False

if (es_nif(dni) == True):
    print("El dni es correcto")
else:
    print("El dni es incorrecto")
