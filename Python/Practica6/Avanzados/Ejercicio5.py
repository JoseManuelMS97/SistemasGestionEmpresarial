class Asignatura:

    def __init__(self, nombre_asignatura, nota):
        self.Nombre_Asignatura = nombre_asignatura
        self.Nota = nota

    def setNota(self, nota):
        self.Nota = nota

    def getNota(self):

        return f"Nota: {self.Nota}"

    def aprobado(self):

        if self.Nota >= 60:
            return "Aprobado"

        else:
            return "Reprobado"

    def __str__(self):

        return f"Asignatura: {self.Nombre_Asignatura}"


class Alumno(Asignatura):

    def __init__(self, nombre, edad, nombre_asignatura="", nota=0):
        Asignatura.__init__(self, nombre_asignatura, nota)

        self.Nombre = nombre
        self.Edad = edad
        self.Asignaturas = dict()

    def setNombre(self, nombre):
        self.Nombre = nombre

    def getNombre(self):

        return f"Nombre: {self.Nombre}"

    def setEdad(self, edad):
        self.Edad = edad

    def getEdad(self):
        return f"Edad: {self.Edad}"

    def promedio(self):

        promedio = 0

        for nota in self.Notas:
            promedio += int(nota)

        promedio /= len(self.Notas)

        return promedio

    def asignatura(self, asignatura):

        if asignatura not in self.Asignaturas:
            self.Asignaturas[asignatura] = 0

    def setNota(self, asignatura, nota):

        self.Asignaturas[asignatura] = nota

    def __str__(self):

        return f"Nombre: {self.Nombre} - Edad: {self.Edad}"


alumnos = list()
alumnos.append(Alumno("Juan", 45))
alumnos.append(Alumno("Ana", 67))
alumnos.append(Alumno("Pedro", 10))

alumnos[0].asignatura("fol")
alumnos[0].asignatura("dam")
alumnos[0].setNota("fol", 84)
alumnos[0].setNota("dam", 10)

print(alumnos[0])
print(alumnos[0].Asignaturas)
print(alumnos[0].aprobado())


