# 2.- Escribir un programa que imprima las 10 tablas de multiplicar.

print("--------TABLAS DE MULTIPLICAR--------")

for i in range(0, 11, 1):
    for j in range(0, 11, 1):
        print(i, "* ", j, " = ", i * j)
    print("--------------------")
