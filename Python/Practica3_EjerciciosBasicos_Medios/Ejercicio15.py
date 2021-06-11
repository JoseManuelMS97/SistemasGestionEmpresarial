# 15.- Escribir un programa que dándole un número (entre 2 y 40) imprima un rombo como el de la
# figura

num = int(input("Nivel (2-40): "))

def dibujar(num):
    val = num
    for i in range(val):
        for j in range(val):
            print("X", end="")

        print(" " * (2 * i), end="")

        for j in range(val):
            print("X", end="")
        print()
        val -= 1

    val += 1
    n_blancos = (num * 2) - 2
    for i in range(num - 1):
        for j in range(val):
            print("X", end="")
        print(" " * n_blancos, end="")

        for j in range(val):
            print("X", end="")
        print()
        n_blancos -= 2
        val += 1

    for j in range(num * 2):
        print("X", end="")


if 2 <= num <= 40:
    dibujar(num)
else:
    print(f"{num} se sale del intervalo (2-40)")