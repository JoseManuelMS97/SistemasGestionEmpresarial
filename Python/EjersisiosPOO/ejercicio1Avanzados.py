# Nombre: Nacho Riquelme
# Fecha: 6/2/21
# Ejercicio 1 Avanzados: Modelar la Clase Diccionario

class Diccionario:

    def __init__(self, nombre, editorial, nivel):

        self.DNombre = nombre
        self.DEditorial = editorial
        self.DNivel = nivel
        self.DPalabras = dict()

    def introducir_palabras(self, palabra):

        if palabra not in self.DPalabras:
            self.DPalabras[palabra] = list()

    def introducir_acepciones(self, palabra, acepcion):

        if palabra in self.DPalabras:
            self.DPalabras.get(palabra).append(acepcion)

    def consultar_palabras(self, palabra=""):

        if palabra == "":
            print(self.DPalabras.items())

        else:
            print(self.DPalabras.get(palabra))

    def ordenar_palabras(self, letra):

        lista = list(self.DPalabras.keys())

        lista.sort()

        for i in lista:

            if i[0] == letra:
                print(i)


# Menú
print(
    '''
    1. Crear el diccionario.
    2. Introducir las palabras.
    3. Introducir acepciones a una palabra.
    4. Consultar palabras y sus acepciones.
    5. Sacar las palabras que empiecen por una letra ordenadas alfabéticamente.
    0. Salir
    ''')

opcion = int(input("Introduce opción: "))

while opcion != 0:

    if opcion == 1:
        nombre_introducido = input("Dime el nombre del diccionario: ").lower()
        editorial_introducida = input("Dime la editorial del diccionario: ").lower()
        nivel_introducido = input("Dime el nivel del diccionario: ").lower()
        diccionario = Diccionario(nombre_introducido, editorial_introducida, nivel_introducido)
        # castellano = Diccionario("Diccionario de la lengua española", "Tricentenario", "Básico")

    elif opcion == 2:
        palabra_introducida = input("Dime la palabra que deseas introducir al diccionario: ").lower()
        diccionario.introducir_palabras(palabra_introducida)
        # castellano.introducir_palabras("Diccionario")

    elif opcion == 3:
        palabra_introducida = input("Dime a qué palabra deseas introducir una acepción: ").lower()
        acepcion_introducida = input("Dime la acepción que deseas introducir a la palabra: ").lower()
        diccionario.introducir_acepciones(palabra_introducida, acepcion_introducida)
        # castellano.introducir_acepciones("Diccionario", "Catálogo de noticias o datos de un mismo género, ordenado "
        #                                                "alfabéticamente.")

    elif opcion == 4:
        palabra_introducida = input("Dime qué palabra deseas consultar (ENTER si deseas ver todas las palabras): ").lower()
        diccionario.consultar_palabras(palabra_introducida)
        # castellano.consultar_palabras("Diccionario")

    elif opcion == 5:
        letra_introducida = input("Dime la primera letra de las palabras que deseas consultar: ").lower()
        diccionario.ordenar_palabras(letra_introducida)
        # castellano.ordenar_palabras("D")

    print(
        '''
    1. Crear el diccionario.
    2. Introducir las palabras.
    3. Introducir acepciones a una palabra.
    4. Consultar palabras y sus acepciones.
    5. Sacar las palabras que empiecen por una letra ordenadas alfabéticamente.
    0. Salir
    ''')

    opcion = int(input("Introduce opción: "))
