
catalogo = {}
n_coches = 0
n_max_coches = 20
salir = False


def alta():
    marca = input("Introduce marca: ")
    modelo = input("Introduce el modelo: ")

    if marca not in catalogo or modelo not in catalogo[marca]:
        cilindrada = input("Introduce cilindrada: ")
        potencia = input("Introduce la potencia: ")
        vel_max = float(input("Introduce la velocidad máxima: "))
        catalogo[marca] = {modelo: [cilindrada, potencia, vel_max]}
        print(f"Coche con marca {marca} y modelo {modelo} dado de alta en el catálogo: ")
    else:
        print("Ya existe ese coche en el catálogo")


def baja():
    if len(catalogo) > 0:
        marca = input("Introduce marca: ")
        modelo = input("Introduce el modelo: ")
        if marca in catalogo and modelo in catalogo[marca]:
            del (catalogo[marca])[modelo]
            print(f"\nCoche con marca {marca} y modelo {modelo} eliminado del catálogo: ")
        else:
            print("\nCoche no disponible en el catálogo: ")
    else:
        print("No existe ningún coche en el catálogo")


def listar():
    if len(catalogo) > 0:
        for marca in catalogo:
            for modelo in catalogo[marca]:
                print(f"Marca: {marca}, modelo: {modelo}, cilindrada: {catalogo[marca][modelo][0]}, "
                      f"potencia: {catalogo[marca][modelo][1]}, velocidad máxima: {catalogo[marca][modelo][2]}")
    else:
        print("No existe ningún coche en el catálogo")


while not salir:
    opcion = int(input("\n1.- Alta coche.\n"
                       "2.- Baja coche\n"
                       "3.- Listar coches.\n"
                       "4.- Salir.\n"
                       "Elija opción (1-4): "))

    if opcion == 1:
        alta()
    elif opcion == 2:
        baja()
    elif opcion == 3:
        listar()
    elif opcion == 4:
        salir = True
    else:
        print("Opción no válida")