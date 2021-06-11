# 9.- Escribir un programa para calcular superficies. Constará de un menú que solicitará la figura a
# la que se va a calcular la superficie, pedirá los datos (lado, base y altura, radio ...) según la figura
# de la que se trate y visualizará el resultado. El programa deberá calcular superficies de las
# siguientes figuras: cuadrados, triángulos y círculos

import math

terminar = False
superficie = 0
while not terminar:
    print("Cálculo de superficies: ")
    print("1.- Cuadrados")
    print("2.- Triángulos")
    print("3.- Círculos")
    print("4.- Salir")

    opcion = int(input("Elija opción (1-4): "))

    if opcion == 1:
        lado = int(input("Lado: "))
        superficie = lado * lado
        print("La superficie es de", superficie, " cm2")
    elif opcion == 2:
        base = int(input("Base: "))
        altura = int(input("Altura: "))
        superficie = (base * altura) / 2
        print("La superficie es de", superficie, " cm2")
    elif opcion == 3:
        radio = int(input("Radio: "))
        superficie = (radio * radio) * math.pi
        print("La superficie es de", superficie, " cm2")
    elif opcion == 4:
        terminar = True