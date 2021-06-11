
# Nombre: Nacho Riquelme
# Fecha: 6/2/21
# Ejercicio 1: Cree   una   clase   COrdenador   para   simular   el   trabajo   con   ordenadores

class COrdenador:

    def __init__(self, marca, procesador, peso, estado=False, pantalla=False):

        self.CMarca = marca
        self.CProcesador = procesador
        self.CPeso = peso
        self.CEstado = estado
        self.CPantalla = pantalla

    def encender_ordenador(self):

        if self.CEstado:
            print("El ordenador está encendido")

        else:
            self.CEstado = True
            self.CPantalla = True
            print("Encendiendo ordenador y pantalla...")

    def apagar_ordenador(self):

        if not self.CEstado:
            print("El ordenador está apagado")

        else:
            self.CEstado = False
            self.CPantalla = False
            print("Apagando ordenador y pantalla...")

    def apagar_pantalla(self):

        if not self.CPantalla:
            print("La pantalla está apagada")

        else:
            self.CPantalla = False
            print("Apagando la pantalla...")

    def encender_pantalla(self):

        if self.CPantalla:
            print("La pantalla está encendida")

        else:
            self.CPantalla = True
            print("Encendiendo la pantalla...")

    def estado_ordenador(self):

        print(f"Marca: {self.CMarca} - Procesador: {self.CProcesador} - Peso: {self.CPeso}")

        if self.CEstado:
            print("El ordenador está encendido")
        else:
            print("El ordenador está apagado")

        if self.CPantalla:
            print("La pantalla está encendida")
        else:
            print("La pantalla está apagada")


# Punto 1 y 2:
OrdenadorCasa = COrdenador("Toshiba", "Intel", 2)
OrdenadorTrabajo = COrdenador("Mitac", "Amd", 3)

print("\nPunto 3:")
OrdenadorCasa.apagar_ordenador()
OrdenadorTrabajo.encender_ordenador()

print("\nPunto 4:")
OrdenadorCasa.estado_ordenador()
OrdenadorTrabajo.estado_ordenador()

print("\nPunto 5:")
OrdenadorTrabajo.apagar_pantalla()

print("\nPunto 6:")
OrdenadorTrabajo.estado_ordenador()

print("\nPunto 7:")
OrdenadorTrabajo.apagar_ordenador()
