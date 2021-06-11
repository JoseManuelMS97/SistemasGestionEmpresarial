class Diccionario:
    def __init__(self, nombre, editorial, nivel, palabras):
        self.nombre = nombre
        self.editorial = editorial
        self.nivel = nivel
        self.palabras = palabras

    def __str__(self):
        return f"Nombre: {self.nombre}, Editorial: {self.editorial}, Nivel: {self.nivel}, Palabras: {self.palabras}"

if __name__ == '__main__':

    diccionario = Diccionario("", "", "", "")

    eleccion = 0
    while eleccion != 6:
        print("1) Crear diccionario.")
        print("2) Introducir palabras.")
        print("3) Introducir aceptaciones a una palabra.")
        print("4) Consultar palabras y sus aceptaciones.")
        print("5) Palabras que empiecen por una letra (ordenadas alfabeticamente).")
        print("6) Finalizar ejecución del programa")
        print()
        eleccion = int(input("Elija una opcion: "))
        if (eleccion == 1):
            nombre = input("Nombre del diccionario nuevo: ")
            editorial = input("Nombre de la editorial: ")
            nivel = input("Nivel del diccionario: ")
            #palabras = input("Palabras que contiene: ")
            diccionario = Diccionario(nombre, editorial, nivel, palabras={})

        elif (eleccion == 2):
            clave = input("Introduce una palabra: ")
            valor = input("Introduce su significcado: ")
            diccionario.palabras[clave] = [valor]

        elif (eleccion == 3):
            clave = input("Palabra a la que desea agregar aceptaciones: ")
            valor = input("Introduce otro significado: ")
            diccionario.palabras[clave] += [valor]

        elif (eleccion == 4):
            print(diccionario.palabras)

        elif (eleccion == 5):
            palabras_letra = []
            letra = input("Introduce una letra: ")
            for palabra in diccionario.palabras:
                if palabra[0] == letra:
                    palabras_letra.append(palabra)
            palabras_ordenadas = sorted(palabras_letra)
            print(palabras_ordenadas)

        elif (eleccion == 6):
            print("FIN DEL PROGRAMA")