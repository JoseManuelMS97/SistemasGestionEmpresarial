# 4.- Escribir un programa que solicite un número positivo, acto seguido debe calcular la suma de
# todos los números pares comprendidos entre 0 y el numero solicitado.

suma = 0

num = int(input("Introduzca un número: "))

for i in range(0, num, 2):
    suma += i

print("La suma es: ",suma)