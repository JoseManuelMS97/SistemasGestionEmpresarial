numeros = []

for i in range(3):
  numero = int(input("Introduce el número #{}: ".format(i + 1)))
  numeros.append(numero)

mayor = numeros[0]
menor = numeros[0]

for numero in numeros:
    if numero > mayor:
        mayor = numero

    if numero < menor:
        menor = numero

print("El mayor es:", mayor)
print("El menor es:", menor)

