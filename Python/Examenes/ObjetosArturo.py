# ExamenObjetos.py
# Nombre: Arturo Lopez Muñoz
# Fecha: 22/02/2021

class Dual():
    def __init__(self, curso):
        self.curso = curso
        self.Alumnos = {}
        self.Empresas = {}

    def __str__(self):
        cadena = ""
        # Recorro todas las keys del diccionario Empresas
        for empresa in self.Empresas:
            # Si su len es mayor que 0 significa que tiene alumnos asi que los recorro con un for y los añado a la cadena
            if len(self.Empresas[empresa]) > 0:
                cadena += "Empresa: {0}\n".format(empresa)
                for alumno in self.Empresas[empresa]:
                    cadena += "\tAlumno: {0}\n".format(alumno[0])
                    cadena += "\tCurso: {0}\n".format(alumno[1])
        return cadena

    def InsertarAlumno(self,nombre, ciclo, curso = 1):
        alumno = [nombre, curso, False]
        # Comprueba si el ciclo no existe y lo crea
        if ciclo not in self.Alumnos.keys():
            self.Alumnos[ciclo] = []
        # Añade Alumno al grupo
        self.Alumnos[ciclo].append(alumno)

    def InsertarEmpresa(self, nombre):
        # Comprueba que la empresa no exista ya, si no es asi la crea
        if nombre not in self.Empresas.keys():
            self.Empresas[nombre] = []
        else:
            print("Esa empresa ya ha sido insertada")

    def AsignarAlumnoEmpresa(self,nombreEmp, nombreAlu, cicloAlu):
        # Busco la empresa en las claves del diccionario empresas
        if nombreEmp not in self.Empresas.keys():
            print("Esa empresa no esta dada de alta, volviendo al menu principal")
        else:
            # Hago lo mismo con el ciclo
            if cicloAlu not in self.Alumnos.keys():
                print("Ese curso no esta dado de alta en la lista de cursos disponibles, volviendo al menu principal...")
            else:
                estaAlu = False
                # Finalmente compruebo si el alumno esta en la lista de alumnos de su ciclo y si es asi lo introduzco en el diccionario por su clave "nombreEmp"
                for i in self.Alumnos[cicloAlu]:
                    if nombreAlu == i[0]:
                        estaAlu = True
                        # Pongo el dato de "practicas" a True
                        i[2] = True
                        self.Empresas[nombreEmp].append(i)
                        print(f"Alumno \"{i[0]}\" asignado para practicas de empresa en \"{nombreEmp}\"")
                if estaAlu == False:
                    print("Ese alumno no esta dado de alta todavia, volviendo al menu principal")

def pedirNumeroEntero():
    correcto = False
    num = 0
    while not correcto:
        try:
            num = int(input("Introduce un numero entero: "))
            correcto = True
        except ValueError:
            print('Error, introduce un numero entero')
    return num

salir = False
opcion = 0

while not salir:

    print("Elige una opcion: \n1. Crear Dual \n2. Introducir Alumno \n3. Introducir Empresa \n4. Asignar Alumno a Empresa"
          "\n5. Sacar Alumnos en Empresas \n0. Salir del programa.")

    opcion = pedirNumeroEntero()

    if opcion == 1:
        dual = Dual("2020-2021")
        print(f"Programa para la gestion de las practicas de alumnos año {dual.curso} creado")

    elif opcion == 2:
        nombre = input("Introduce nombre de alumno: ")
        ciclo = input("Que ciclo esta cursando el alumno?: ")
        curso = int(input("Introduce el curso: "))
        dual.InsertarAlumno(nombre,ciclo, curso)
    elif opcion == 3:
        nombre = input("Introduce el nombre de la empresa que deseas insertar: ")
        dual.InsertarEmpresa(nombre)
    elif opcion == 4:
        nombreAlu = input("Introduce nombre de alumno: ")
        nombreEmp = input("Introduce el nombre de la empresa: ")
        cicloAlu = input("Que ciclo esta cursando el alumno?: ")
        dual.AsignarAlumnoEmpresa(nombreEmp, nombreAlu, cicloAlu)
    elif opcion == 5:
        print(dual, end=" ")
    elif opcion == 0:
        salir = True
    else:
        print("Introduce un numero entre 0 y 5")
print("Fin")