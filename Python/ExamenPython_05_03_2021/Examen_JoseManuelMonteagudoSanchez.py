# Examen POO - 05/03/2021 - Jose Manuel Monteagudo Sanchez

#Clase Tren
class Tren:
    def __init__(self, nombre, nVagones=2):

        self.Nombre = nombre
        self.NVagones = nVagones
        self.NAsientos = 4
        self.Vagones = dict()

    # Método que rellena vagones al iniciar el programa
    def rellenarVagones(self):

        for numeroVagon in range(self.NVagones):

            self.Vagones[numeroVagon] = list()

            for numeroAsiento in range(self.NAsientos):
                self.Vagones[numeroVagon].append(False)

    #Devuelve los asientos libres
    def AsientosLibres(self):

        contador = 0

        for vagones in self.Vagones.values():

            for asientosLibres in vagones:
                if not asientosLibres:
                    contador += 1

        return contador

    #Compra billetes
    def ComprarBilletesSeparados(self, billetes):

        asientosLibres = self.AsientosLibres()

        if asientosLibres >= billetes:

            contador = 0
            numeroVagon = 0

            asientosOcupados = dict()

            while contador < billetes:

                asientosOcupados[numeroVagon] = list()

                for asientos in range(self.NAsientos):

                    if contador < billetes and not self.Vagones[numeroVagon][asientos]:
                        self.Vagones[numeroVagon][asientos] = True
                        asientosOcupados[numeroVagon].append(asientos)
                        contador += 1

                numeroVagon += 1

            self.devolverResultadoAsientosLibres(asientosOcupados)

        else:
            print(f"No hay asientos suficientes, solo quedan {asientosLibres}")

    #Compra billetes si hay disponibles en el mismo vagon
    def ComprarBilleteJuntos(self, billetes):

        asientosLibres = self.AsientosLibres()

        if asientosLibres >= billetes and billetes < 5:

            contador = 0
            numeroVagon = 0
            finalVagones = 0
            asientosPosibles = False

            asientosOcupados = dict()

            while finalVagones < self.NVagones and not asientosPosibles:

                for asientos in range(self.NAsientos):

                    if contador < billetes and not self.Vagones[numeroVagon][asientos]:
                        contador += 1

                if contador == billetes:
                    asientosPosibles = True

                    asientosOcupados[numeroVagon] = list()

                    for asientos in range(self.NAsientos):

                        if billetes > 0 and not self.Vagones[numeroVagon][asientos]:
                            self.Vagones[numeroVagon][asientos] = True
                            asientosOcupados[numeroVagon].append(asientos)
                            billetes -= 1

                    self.devolverResultadoAsientosLibres(asientosOcupados)

                else:
                    asientosOcupados[numeroVagon] = list()
                    numeroVagon += 1
                    contador = 0


        else:
            print(f"No hay billetes en los mismos vagones.")

    # Método que devuelve el resultado
    def devolverResultadoAsientosLibres(self, asientosOcupados):

        for vagon in asientosOcupados:

            print(f"Vagón: {vagon}")
            print(f"Asientos: ", end="")

            for asiento in asientosOcupados[vagon]:
                print(f"{asiento} - ", end="")

            print("")

def menu():
    return f"\n1. Crear Tren" \
           f"\n2. Asientos Libres" \
           f"\n3. Comprar Billetes Separados" \
           f"\n4. Comprar Billetes Juntos" \
           f"\n5. Salir" \
           f"\nOpción: "


if __name__ == '__main__':
    opcion = 0

    while opcion != "5":
        opcion = input(menu())

        if opcion == "1":
            nombre = input("Introduce el nombre para el tren: ")
            tren = Tren(nombre)
            tren.rellenarVagones()
            print(f"Se ha creado el tren {nombre}.")

        elif opcion == "2":
            print(f"Asientos Libres: {tren.AsientosLibres()}")

        elif opcion == "3":
            cantidad = int(input("Introduce la cantidad de billetes a comprar: "))
            tren.ComprarBilletesSeparados(cantidad)

        elif opcion == "4":
            cantidad = int(input("Introduce la cantidad de billetes a comprar: "))
            tren.ComprarBilleteJuntos(cantidad)

        elif opcion == "5":
            print("FIN DEL TRAYECTO.")