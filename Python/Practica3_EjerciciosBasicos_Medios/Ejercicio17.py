# 17.- Escribir un programa que haga que el usuario piense un número entero de 1 a 100, el
# programa deberá adivinarlo en el menor número de intentos posible. Al final debe decir en
# cuántos intentos lo ha conseguido

import random

print("Piense un número del 0 al 100 (no me engañe ni cambie de número)")
input("ENTER para comenzar")

def adivina():
    acierto = False
    n_intentos = 0
    limInf = 0
    limSup = 100

    while not acierto:
        n_intentos += 1

        if limSup <= limInf:
            print("No puede cambiar el número a mitad del juego")
            n_intentos = 0
            limInf = 1
            limSup = 100

        num = random.randint(limInf, limSup)
        resp = input(f"¿es el {num}? (m-mayor, n-menor, i-igual)")

        if resp == "m":
            if num == 100:
                print(f"El número no puede ser mayor que 100, piense en otro número")
                n_intentos = 0
                limInf = 1
                limSup = 100
            else:
                limInf = num + 1
        if resp == "n":
            if num == 1:
                print(f"El número no puede ser menor que 0, piense en otro número")
                n_intentos = 0
                limInf = 1
                limSup = 100
            else:
                limSup = num - 1
        if resp == "i":
            print(f"¡¡¡Qué bueno soy, lo he acertado en tan sólo {n_intentos} intentos!!!")
            volver_jugar = input("¿Desea jugar otra vez (S/N)?").upper()
            if volver_jugar == "N":
                acierto = True
                print("\n¡Adios!")
            else:
                n_intentos = 0
                limInf = 1
                limSup = 100

adivina()