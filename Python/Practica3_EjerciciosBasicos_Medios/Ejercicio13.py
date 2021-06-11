# 13.- Escribir un programa que solicite un número n y a continuación imprima todos los números
# primos comprendidos en el intervalo [2-n].

cont = 0
num = int(input("Introduzca un número: "))
print("Números primos [2 -", num, "]: ")
for n in range(1, num + 1):
    for d in range(1, n + 1):
        if n % d == 0:
            cont += 1
    if cont == 2:
        print("{}".format(n), end=", ")
    cont = 0
