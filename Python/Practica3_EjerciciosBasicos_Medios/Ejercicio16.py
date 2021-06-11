# 16.- Escribir un programa para que dada una cantidad de euros la devuelva en el menor número
# de billetes y monedas de curso legal posible (billetes: 500 €, 200 €, 100 €, 50 €, 20 €, 10 € y 5€.
# Monedas: 2 €, 1 €

cantidad = int(input("Introduzca una cantidad: "))
lista = [500, 200, 100, 50, 20, 10, 5, 2, 1]

for i in lista:
    queda = cantidad // i
    cantidad = cantidad % i
    if  queda > 0:
        print(str(queda)+  (" billete" if i > 2 else " moneda") +("s de " if queda >1 else " de ")+ str(i))