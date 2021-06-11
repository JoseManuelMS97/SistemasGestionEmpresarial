class Persona:

    def __init__(self, nif, nombre, apellidos, edad):
        self.nif = nif
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = edad

    def medad(self):
        print(self.edad)

    def mnombre(self):
        print(self.nombre)

    def mnif(self):
        print(self.nif)

    def mapellidos(self):
        print(self.apellidos)

    def mostrar_nombre_completo(self):
        print(f"Nombre: {self.nombre}, Apellidos: {self.apellidos}")

    def __str__(self):
        return f"DNI: {self.nif}, Nombre: {self.nombre}, Apellidos: {self.apellidos}, Edad: {self.edad}"


class Alumno(Persona):

    def __init__(self, nif, nombre, apellidos, edad, curso):
        Persona.__init__(self, nif, nombre, apellidos, edad)
        self.curso = curso

    def mcurso(self):
        print(self.curso)

    def mostrar_nombre_completo(self):
        print(f"Nombre: {self.nombre}, Apellidos: {self.apellidos}, Curso: {self.curso}")

    def __str__(self):
        return f"DNI: {self.nif}, Nombre: {self.nombre}, Apellidos: {self.apellidos}, Edad: {self.edad}, Curso: {self.curso}"

if __name__ == '__main__':
    persona = Persona("12345678A", "Jose", "Sanchez", 24)
    alumno = Alumno("98765432B", "Pablo", "Lopez", 25, "2º DAM")

    print(persona.__str__())
    print(alumno.__str__())
    print("\n")

    persona.mostrar_nombre_completo()
    alumno.mostrar_nombre_completo()
    alumno.mcurso()