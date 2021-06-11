# 11.- Escribir un programa que calcule el factorial de un número dado.

num = int(input("Introduce un número: "))
factorial = 1

for n in range(1, num+1):
    factorial = factorial * n

print(num, "! = ", factorial)