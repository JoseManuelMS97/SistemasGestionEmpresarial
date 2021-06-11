# 14.- Escribir un programa que dándole un número (entre 2 y 40) imprima un triángulo como el de
# la figura.

def Piramide(lineas):
    for i in range(lineas):
        print(' ' * (lineas - i - 1) + '*' * (2 * i + 1))


lineas = int(input("Nivel: "))
if 2 < lineas < 40:
    Piramide(lineas)
else:
    print("El nivel debe ser entre 2 y 40.")