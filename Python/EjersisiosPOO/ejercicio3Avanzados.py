# Nombre: Nacho Riquelme
# Fecha: 7/2/21
# Ejercicio 3 Avanzados: Crear una aplicacion para gestionar un videoclub.

class Videoclub:

    def __init__(self, titulo, tipo, precio_alquiler, plazo_alquiler, alquilada="No"):
        self.Titulo = titulo
        self.Tipo = tipo
        self.Precio_Alquiler = precio_alquiler
        self.Plazo_Alquiler = plazo_alquiler
        self.Alquilada = alquilada

    def __repr__(self):
        return f"Titulo: {self.Titulo} - Tipo: {self.Tipo} - Precio Alquiler: {self.Plazo_Alquiler} - " \
               f"Plazo Alquiler: {self.Plazo_Alquiler} - Alquilada: {self.Alquilada}"


class Pelicula(Videoclub):
    def __init__(self, titulo, tipo, precio_alquiler, plazo_alquiler, alquilada, genero="", anio=0, director="",
                 interpretes=""):
        Videoclub.__init__(self, titulo, tipo, precio_alquiler, plazo_alquiler, alquilada)

        generos = ["accion", "fantastica", "drama", "aventuras", "puzzle", "infantil"]

        if genero not in generos:
            self.Genero = ""
        else:
            self.Genero = genero

        self.Anio = anio
        self.Director = director
        self.Interpretes = interpretes

    def __repr__(self):
        return f"Titulo: {self.Titulo} - Tipo: {self.Tipo} - Precio Alquiler: {self.Plazo_Alquiler} - " \
               f"Plazo Alquiler: {self.Plazo_Alquiler} - Alquilada: {self.Alquilada} - " \
               f"Género: {self.Genero} - Año: {self.Anio} - Intérpretes: {self.Interpretes}"


class Videojuego(Videoclub):
    def __init__(self, titulo, tipo, precio_alquiler, plazo_alquiler, alquilada, estilo="", plataforma=""):
        Videoclub.__init__(self, titulo, tipo, precio_alquiler, plazo_alquiler, alquilada)

        estilos = ["accion", "deportes", "aventuras", "puzzle", "infantil"]

        if estilo not in estilos:
            self.Estilo = ""
        else:
            self.Estilo = estilo

        plataformas = ["xbox", "playstation", "wii"]

        if plataforma not in plataformas:
            self.Plataforma = ""
        else:
            self.Plataforma = plataforma

    def __repr__(self):
        return f"Titulo: {self.Titulo} - Tipo: {self.Tipo} - Precio Alquiler: {self.Plazo_Alquiler} - " \
               f"Plazo Alquiler: {self.Plazo_Alquiler} - Alquilada: {self.Alquilada} - " \
               f"Estilo: {self.Estilo} - Plataforma: {self.Plataforma}"


class Cliente:

    def __init__(self, numero_cliente, nombre, direccion, telefono, *productos_alquilados):
        self.Numero_Cliente = numero_cliente
        self.Nombre = nombre
        self.Direccion = direccion
        self.Telefono = telefono
        self.Productos_Alquilados = productos_alquilados

    def __repr__(self):
        return f"Número de cliente: {self.Numero_Cliente} - Nombre: {self.Nombre} - Dirección: {self.Direccion} - " \
               f"Teléfono: {self.Telefono} - Productos Alquilados: {self.Productos_Alquilados}"


videoclub = dict()
videoclub["peliculas"] = dict()
videoclub["videojuegos"] = list()

clientes = dict()

print(
    '''
    1. Añadir producto.
    2. Listar productos.
    3. Ficha producto.
    4. Añadir cliente.
    5. Listar clientes.
    6. Ficha cliente.
    7. Alquiler producto.
    0. Salir.
    ''')

opcion = int(input("Introduce opción: "))

while opcion != 0:

    if opcion == 1:

        videoclub["peliculas"]["Star Wars"] = list()
        videoclub["peliculas"]["Star Wars"].append(
            Pelicula("Star Wars", "Pelicula", 3, 2, "No", "accion", 1969, "George Lucas",
                     "Mark Hamill"))

        videoclub["peliculas"]["Lord of the Rings"] = list()
        videoclub["peliculas"]["Lord of the Rings"].append(
            Pelicula("Lord of the Rings", "Pelicula", 2, 1, "Sí", "accion", 1969,
                     "Peter Jackson", "Elijah Wood"))

    elif opcion == 2:

        for pelicula in videoclub["peliculas"].items():
            print(pelicula)

    elif opcion == 3:
        pelicula = input("Dime la película: ")

        if pelicula not in videoclub["peliculas"]:
            print("No existe la película en el videoclub")

        else:
            print(videoclub["peliculas"][pelicula])

    elif opcion == 4:
        clientes["Juan"] = list()
        clientes["Juan"].append(Cliente(1, "Juan", "Calle Prueba", 612348674, "Star Wars", "Lord of the Rings"))

    elif opcion == 5:
        for cliente in clientes.items():
            print(cliente)

    elif opcion == 6:
        cliente = input("Dime el número de cliente: ")

        if pelicula not in videoclub["peliculas"]:
            print("No existe el cliente")

        else:
            print(clientes["cliente"])

    print(
        '''
        1. Añadir producto.
        2. Listar productos.
        3. Ficha producto.
        4. Añadir cliente.
        5. Listar clientes.
        6. Ficha cliente.
        0. Salir.
        ''')

    opcion = int(input("Introduce opción: "))
