# 12.- Escribir un programa que solicite un número n y a continuación muestre si el número es o no
# primo

def esPrimo(num):
    if num < 1:
        return False
    elif num == 2:
        return True
    else:
        for n in range(2, num):
            if num % n == 0:
                return False
        return True

num = int(input("Introduzca un número: "))
if esPrimo(num):
    print("El número es primo")
else:
    print("El número no es primo")