
# Nombre: Nacho Riquelme
# Fecha: 6/2/21
# Ejercicio 1b: Modificar el ejercicio anterior

class COrdenador:

    def __init__(self, marca, procesador, peso, estado=False, pantalla=False):

        self.CMarca = marca
        self.CProcesador = procesador
        self.__CPeso = peso
        self.CEstado = estado
        self.CPantalla = pantalla

    def get_peso(self):
        return self.__CPeso

    def set_peso(self, peso):

        if peso < 1:
            self.__CPeso = 1

        else:
            self.__CPeso = peso

    CPeso = property(get_peso, set_peso)

    def __str__(self):

        cadena = f"Marca: {self.CMarca} - Procesador: {self.CProcesador} - Peso: {self.CPeso}"
        return cadena


OrdenadorCasa = COrdenador("Toshiba", "Intel", 2)
OrdenadorTrabajo = COrdenador("Mitac", "Amd", 3)

print(OrdenadorCasa)
print(OrdenadorTrabajo)

OrdenadorTrabajo.set_peso(0)
print(OrdenadorTrabajo)

OrdenadorTrabajo.set_peso(10)
print(OrdenadorTrabajo)
