#Nombre: Jose Manuel Monteagudo Sanchez
#Fecha: 19/02/2021
#Examen Python POO

class Vacunados:
    def __init__(self,comunidad = "Murcia"):
        self.Comunidad = comunidad
        self.ciudadanos = list()
        self.NoVacunados = dict()

    def InsertarCiudadano(self, grupo, nombreCiudadano):
        numeroVacunas = 0
        self.ciudadanos.append([nombreCiudadano, numeroVacunas])

        if grupo not in self.NoVacunados.keys():
            self.NoVacunados[grupo] = [nombreCiudadano, numeroVacunas]
        else:
            self.NoVacunados[grupo] += [nombreCiudadano, numeroVacunas]


    def LleganVacunas(self, cantidad):

        while cantidad != 0:
            for grupo in self.NoVacunados.keys():
                if self.NoVacunados[grupo][1] < 2:
                    self.NoVacunados[grupo][1] += 1
                    cantidad -= 1
                else:
                    self.NoVacunados.pop(grupo)

    def __str__(self):
        ciudadanos = 0
        noVacunados = 0
        vacunadosParcialmente = 0
        vacunadosTotalmente = 0

        for c in self.ciudadanos:
            ciudadanos+=1

        for grupo in self.NoVacunados.keys():
            if self.NoVacunados[grupo][1] == 0:
                noVacunados += 1

        for grupo in self.NoVacunados.keys():
            if self.NoVacunados[grupo][1] == 1:
                vacunadosParcialmente += 1

        for grupo in self.NoVacunados.keys():
            if self.NoVacunados[grupo][1] == 2:
                vacunadosTotalmente += 1

        return f"Poblacion Total: {ciudadanos}\nNumero de Ciudadanos sin Vacunar: {noVacunados}\nNumero de Ciudadanos Vacunados Parcialmente: {vacunadosParcialmente}\nNumero de Ciudadanos Vacunados Totalmente: {vacunadosTotalmente}\nCiudadanos sin ninguna vacuna por niveles:\nNivel 4:\nNivel 5:\n"


eleccion = 0
vacunados = None
while eleccion != 5:
    print("1) Crear Vacunas.")
    print("2) Introducir Ciudadano.")
    print("3) Llegan Vacunas.")
    print("4) Mostrar informacion")
    print("5) Finalizar ejecución del programa")
    print()
    eleccion = int(input("Elija una opcion: "))

    if (eleccion == 1):
        vacunados = Vacunados()
        print("Se ha creado el objeto de la clase Vacunados.\n")

    elif(eleccion == 2):
        grupo = int(input("Introduce el numero del grupo al que pertenece: "))
        nombre = input("Introduce el nombre del ciudadano: ")

        vacunados.InsertarCiudadano(grupo,nombre)
    elif(eleccion == 3):
        cantidad = int(input("Introduzca la cantidad de vacunas que ha llegado: "))
        vacunados.LleganVacunas(cantidad)
        print("Han sido vacunados.\n")

    elif(eleccion == 4):
        print(vacunados)

    elif(eleccion == 5):
        print("\nFIN DEL PROGRAMA")
