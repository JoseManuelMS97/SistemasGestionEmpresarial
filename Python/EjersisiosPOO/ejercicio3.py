# Nombre: Nacho Riquelme
# Fecha: 6/2/21
# Ejercicio 3: Crear una clase Persona con los siguientes miembros.

class Persona:

    def __init__(self, nif=None, nombre=None, apellidos=None, edad=0):
        self.PNif = nif
        self.PNombre = nombre
        self.PApellidos = apellidos
        self.PEdad = edad

    def medad(self):
        return f"Edad: {self.PEdad}"

    def mnombre(self):
        return f"Nombre: {self.PNombre}"

    def mapellidos(self):
        return f"Apellidos: {self.PApellidos}"

    def mnif(self):
        return f"DNI: {self.PNif}"

    def mostrar_nombre_completo(self):
        return f"Nombre y apellidos: {self.PNombre} {self.PApellidos}"

    def __str__(self):
        return f"DNI: {self.PNif} - Nombre: {self.PNombre} - Apellidos: {self.PApellidos} - " \
                 f"Edad: {self.PEdad}"


class Alumno(Persona):

    def __init__(self, nif, nombre, apellidos, edad, curso=None):
        Persona.__init__(self, nif, nombre, apellidos, edad)

        self.ACurso = curso

    def mcurso(self):
        return f"Curso: {self.ACurso}"

    def mostrar_nombre_completo(self):
        super(Alumno, self).mostrar_nombre_completo()

        return f"Nombre y apellidos: {self.PNombre} {self.PApellidos} - Curso: {self.ACurso}"

    def __str__(self):
        return f"DNI: {self.PNif} - Nombre: {self.PNombre} - Apellidos: {self.PApellidos} - " \
               f"Edad: {self.PEdad} - Curso: {self.ACurso}"


Juan = Persona("12345678Z", "Juan", "García Pérez", 28)
Ana = Alumno("48651755Q", "Ana", "Martínez Rodríguez", 21, "1º DAM")

print(Juan)
print(Juan.mostrar_nombre_completo())
print("")
print(Ana)
print(Ana.mostrar_nombre_completo())
