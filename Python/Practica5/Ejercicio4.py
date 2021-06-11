dni = input("Introduzca su dni sin letra: ")


def letra_nif(dni):
    letras = "TRWAGMYFPDXBNJZSQVHLCKE"

    if len(dni) == 8:
        letra = letras[int(dni) % 23]
        dni += letra
        return dni


if (len(dni) == 8):
    print("El dni con la letra seria: " + letra_nif(dni))
else:
    print("El dni debe tener 8 digitos.")
