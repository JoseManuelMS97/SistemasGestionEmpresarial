# !/usr/bin/env python3
# 2
__author__ = "Ramón Moñino Rubio"
__email__ = "ramonmr16@gmail.com"
__version__ = "1.0.0"


class Establecimiento:

    def __init__(self, nombre):
        self.nombre = nombre
        self.opiniones = {}

    def insertar_opinion(self, pais="España"):
        punt = float(input("Introduce la puntuación: "))

        if punt > 10:
            punt = 10
        elif punt < 1:
            punt = 1

        comentario = input("Introduce el comentario: ")
        if pais not in self.opiniones:
            self.opiniones[pais] = []
        self.opiniones[pais].append((punt, comentario))

    def media(self):
        sum = 0
        votos = {}
        num = 0

        for p in self.opiniones.keys():
            for i in range(len(self.opiniones[p])):
                if self.opiniones[p][i][0] not in votos.keys():
                    votos[int(self.opiniones[p][i][0])] = 1
                else:
                    votos[int(self.opiniones[p][i][0])] += 1
                sum += self.opiniones[p][i][0]
                num += 1

        media = sum / num

        print(f"Establecimiento: {self.nombre}")
        print(f"Puntuación: {media} ", end="")
        print("*" * int(media))
        print()

        for i in votos:
            print(f"{i}: {votos[i]}")


def menu():
    return f"\n1. Crear Establecimiento. " \
           f"\n2. Introducir Opinión. " \
           f"\n3. Media. " \
           f"\n4. Salir. "


if __name__ == '__main__':
    opcion = input(menu())

    establecimiento = Establecimiento("Pais")

    while opcion != "4":
        if opcion == "1":
            nom = input("Introduce el nombre del estableciento: ")
            establecimiento = Establecimiento(nom)

        elif opcion == "2":
            pais = input("Introduce el pais: ")
            establecimiento.insertar_opinion(pais)

        elif opcion == "3":
            n_pais = input("Introduce el nombre del país: ")
            establecimiento.media()

        elif opcion == "4":
            print("Hasta pronto!")

        opcion = input(menu())
