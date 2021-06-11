#Axel Lopez Perez

class Vacunados:
    def __init__(self, Comunidad="Murcia"):
        self.Comunidad = Comunidad
        self.Ciudadanos = []
        self.NoVacunados = {}

    def InsertarCiudadano(self, grupo, nombre):
        #Añade ciudadano a la lista
        self.Ciudadanos.append([nombre, 0])

        #Comprueba si el grupo no existe y lo crea
        if grupo not in self.NoVacunados.keys():
            self.NoVacunados[grupo] = []
        #Añade ciudadano al grupo
        self.NoVacunados[grupo].append(self.Ciudadanos[-1])

    def LLeganVacunas(self, cantidad):
        grupos_vacios = []
        while cantidad > 0:
            for grupo in self.NoVacunados:
                for ciud in self.NoVacunados[grupo]:
                    #Se vacuna al ciudadano
                    if cantidad >= 2:
                        ciud[1] += 2
                        cantidad -= 2
                    elif cantidad > 0:
                        ciud[1] += 1
                        cantidad -= 1
                    #Si el ciudadado ha recibido sus 2 vacunas, se elimina
                    if ciud[1] == 2:
                        self.NoVacunados[grupo].remove(ciud)

                #Si no queda ningun ciudadado en el grupo, se añade a la lista para borrar
                if len(self.NoVacunados[grupo]) == 0:
                    grupos_vacios.append(grupo)

        #Se eliminan los grupos vacios
        for grupo in grupos_vacios:
            self.NoVacunados.pop(grupo)
            print(f"{grupo} eliminado")
                        

    def __str__(self):
        sin_vacunar = 0
        vac_parciales = 0
        poblacion = len(self.Ciudadanos)
        for grupo in self.NoVacunados:
            print(self.NoVacunados[grupo])
            sin_vacunar += len(self.NoVacunados[grupo])
            for ciud in self.NoVacunados[grupo]:
                if ciud[1] == 1:
                    vac_parciales += 1

        vac_totales = poblacion - sin_vacunar

        return f"Población Total: {poblacion}" \
            f"\nNúmero de Ciudadanos sin Vacunar: {sin_vacunar} ({(sin_vacunar * 100) / poblacion}%)" \
            f"\nNúmero de Ciudadanos Vacunados Parcialmente: {vac_parciales} ({(vac_parciales * 100) / poblacion}%)" \
            f"\nNúmero de Ciudadanos Vacunados Totalmente: {vac_totales} ({(vac_totales * 100) / poblacion}%)"

def menu():
    return f"\n1. Crear Vacunas" \
        f"\n2. Introducir Ciudadano" \
        f"\n3. Llegan Vacunas" \
        f"\n4. Mostrar Información" \
        f"\n5. Salir" \
        f"\nOpción: "

if __name__ == '__main__':
    opcion = input(menu())
    
    while opcion != "5":
        if opcion == "1":
            vacunados = Vacunados()

        elif opcion == "2":
            grupo = input("Grupo del ciudadano: ")
            nombre = input("Nombre del ciudadano: ")
            vacunados.InsertarCiudadano(grupo, nombre)

        elif opcion == "3":
            cantidad = int(input("Cantidad de vacunas: "))
            vacunados.LLeganVacunas(cantidad)

        elif opcion == "4":
            print(vacunados)

        opcion = input(menu())
        