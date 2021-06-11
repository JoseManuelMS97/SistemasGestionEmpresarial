import math

unidades = ["cero", "uno", "dos", "tres", "cuatro", "cinco",
            "seis", "siete", "ocho", "nueve", "diez"]
especiales = ["once", "doce", "trece", "catorce", "quince",
              "dieciseis", "diecisiete", "dieciocho", "diecinueve"]
decenas = ["veinte", "treinta", "cuarenta", "cincuenta", "sesenta",
           "setenta", "ochenta", "noventa"]

num = int(input("Ingrese un numero entre 0 y 100: "))

if 0 <= num < 11:
    print("El numero es el ", unidades[num])

elif num < 20:
    print("El numero es el ", especiales[num - 11])

elif num < 100:

    unid = num % 10
    dec = int(math.floor(num / 10))
    if unid == 0:
        print("El numero es el ", decenas[dec - 2])
    else:
        print("El numero es el ", decenas[dec - 2], "y", unidades[unid])
else:
    print("El numero debe ser menor a 100")
