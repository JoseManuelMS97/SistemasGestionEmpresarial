# 1.- Programa que lee un número y muestra la tabla de multiplicar de dicho número.

numero = int(input("Numero: "))

for i in range(0, 11, 1):
    print(numero, "* ", i, " = ", numero * i)
