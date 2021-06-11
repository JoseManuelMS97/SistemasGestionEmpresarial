# 7.- Escribir un programa que solicite números (enteros o reales), el programa terminará cuando
# se introduzca el cero. A continuación debe mostrar el mayor número.

num = int(input("Introduzca un número (cero para terminar):"))
mayor = num

while not (num == 0):
    if num > mayor:
        mayor = num
    num = int(input("Introduzca un número (cero para terminar):"))

print("Mayor: ", mayor)
