# 5.- Escribe un programa que dado un número, muestre todos los múltiplos de 11 desde el cero
# hasta el número.

suma = "0"

num = int(input("Introduzca un número: "))

for i in range(11, num+1, 11):
    suma += " , "
    suma += str(i)

print("Los multiplos son: ",suma)