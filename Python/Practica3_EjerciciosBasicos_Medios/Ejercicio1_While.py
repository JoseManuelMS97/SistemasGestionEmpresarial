# 1.- Programa que lee un número y muestra la tabla de multiplicar de dicho número.

numero = int(input("Numero: "))

i = 0
while i <= 10:
    print(numero, "* ", i, " = ", numero * i)
    i += 1
