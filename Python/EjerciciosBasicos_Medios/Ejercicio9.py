numeros = input("Introduzca 4 numeros enteros: ")
numero = numeros.split()

mayor = numero[0]
menor = numero[0]

for n in numero:
    if n > mayor:
        mayor = n
    if n < menor:
        menor = n

print("Mayor numero: ", mayor)
print("Menor numero: ", menor)
