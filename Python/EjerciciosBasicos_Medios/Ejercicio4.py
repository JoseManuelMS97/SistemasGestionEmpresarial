from math import sqrt

a = int(input("Ingrese el coeficiente de la variable cuadrática\n"))
b = int(input("Ingrese el coeficiente de la variable lineal\n"))
c = int(input("Ingrese el término independiente\n"))
x1= 0
x2= 0
if ((b**2)-4*a*c) < 0:
  print("La solución de la ecuación es con números complejos")
else:
  x1 = (-b+sqrt(b**2-(4*a*c)))/(2*a)
  x2 = (-b-sqrt(b**2-(4*a*c)))/(2*a)
  print("Las soluciones de la ecuación son:")
  print(x1)
  print(x2)