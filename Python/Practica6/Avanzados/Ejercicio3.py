import datetime


class Producto:

    def __init__(self, referencia, precio_alquiler, plazo_alquiler):
        self.referencia = referencia
        self.precio_alquiler = precio_alquiler
        self.plazo_alquiler = plazo_alquiler
        self.alquilado = False

    def __str__(self):
        return f"Referencia: {self.referencia}, Precio alquiler: {self.precio_alquiler}, " \
               f"Plazo alquiler: {self.plazo_alquiler}, Alquilado: {self.alquilado}"


class Pelicula(Producto):

    def __init__(self, referencia, precio_alquiler, plazo_alquiler, alquilado, genero, anyo, director, interpretes):
        Producto.__init__(self, referencia, precio_alquiler, plazo_alquiler)
        self.genero = genero
        self.anyo = anyo
        self.director = director
        self.interpretes = interpretes


class Videojuego(Producto):

    def __init__(self, referencia, precio_alquiler, plazo_alquiler, estilo, plataforma):
        Producto.__init__(self, referencia, precio_alquiler, plazo_alquiler)
        self.estilo = estilo
        self.plataforma = plataforma


class Cliente:

    def __init__(self, numero, nombre, direccion, telefono, productos_alquilados):
        self.numero = numero
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono
        self.productos_alquilados = productos_alquilados

    def __str__(self):
        return f"Número: {self.numero}, nombre: {self.nombre}, direccion: {self.direccion}, telefono: {self.telefono}" \
               f", productos alquilados: {mostrar_productos(self.productos_alquilados)}"


class Alquiler:

    def __init__(self, n_cliente, producto, fecha_alquiler, fecha_devolucion, importe):
        self.n_cliente = n_cliente
        self.producto = producto
        self.fecha_alquiler = fecha_alquiler
        self.fecha_devolucion = fecha_devolucion
        self.importe = importe


def mostrar_productos(prods):
    for p in prods:
        print(p)


def mostrarMenu():
    return f"\n1 – Lista productos\n" \
           f"2 – Añadir producto\n" \
           f"3 – Ficha producto\n" \
           f"4 – Lista clientes\n" \
           f"5 – Añadir cliente\n" \
           f"6 – Ficha cliente\n" \
           f"7 – Alquiler producto\n" \
           f"8 – Listar Alquiler\n" \
           f"9 - Salir\n" \



if __name__ == '__main__':
    lst_productos = []
    lst_clientes = []
    lst_registro = []
    salir = False

    while not salir:
        opcion = input(mostrarMenu())

        if opcion == "1":
            if len(lst_productos) > 0:
                for prod in lst_productos:
                    print(prod)
            else:
                print("No existe ningún producto.")

        elif opcion == "2":
            titulo = input("Introduce el titulo: ")
            tipo = input("Tipo (pelicula/videojuego): ")
            pre_alquiler = int(input("Precio alquiler: "))
            pla_alquiler = int(input("Plazo alquiler: "))
            producto = Producto([titulo, tipo], pre_alquiler, pla_alquiler)
            lst_productos.append(producto)

        elif opcion == "3":
            encontrado = False
            i = 0
            tit = input("Introduce el titulo de la película: ")

            while not encontrado and i < len(lst_productos):
                if lst_productos[i].referencia[0] == tit:
                    encontrado = True
                    print(lst_productos[i])
                i += 1

            if not encontrado:
                print("El producto no existe.")

        elif opcion == "4":
            if len(lst_clientes) > 0:
                for cli in lst_clientes:
                    print(cli)
            else:
                print("No hay ningún cliente.")

        elif opcion == "5":
            num = input("Introduce el número de cliente; ")
            nom = input("Introduce el nombre del cliente: ")
            direcc = input("Introduce la dirección: ")
            tlf = input("Introduce el tlf: ")
            prod_alquilados = input("Introduce productos (separados por ,): ").replace(" ", "").split(",")
            cliente = Cliente(num, nom, direcc, tlf, prod_alquilados)
            lst_clientes.append(cliente)

        elif opcion == "6":
            encontrado = False
            i = 0
            num = input("Introduce el número de cliente: ")

            while not encontrado and i < len(lst_clientes):
                if lst_clientes[i].numero == num:
                    print(lst_clientes[i])
                    encontrado = True
                i += 1

            if not encontrado:
                print("El cliente no existe.")

        elif opcion == "7":
            encontrado = False
            i = 0
            num = input("Introduce el número de cliente: ")

            while not encontrado and i < len(lst_clientes):
                if lst_clientes[i].numero == num:
                    cliente = lst_clientes[i]
                    encontrado = True
                i += 1

            if encontrado:
                titulo = input("Introduce el titulo: ")
                tipo = input("Tipo: ")
                pre_alquiler = int(input("Precio alquiler: "))
                pla_alquiler = int(input("Plazo alquiler: "))
                producto = Producto([titulo, tipo], pre_alquiler, pla_alquiler)
                cliente.productos_alquilados.append(producto)

                fech_alquiler = datetime.datetime.now()
                fech_dev = fech_alquiler + datetime.timedelta(days=15)

                importe = float(input("Introduce el importe: "))

                alquiler = Alquiler(num, producto, fech_alquiler, fech_dev, importe)
                lst_registro.append(alquiler)
            else:
                print("El cliente no existe.")

        elif opcion == "8":
            salir = True