# Nombre: Nacho Riquelme
# Fecha: 6/2/21
# Ejercicio 2 Avanzados: La empresa informática “IPMTech” necesita llevar un registro de todos sus empleados
# que se encuentran en la oficina central, para eso ha creado un diagrama de clases que debe incluir lo siguiente

class Empleado:

    def __init__(self, nombre="", edad=0, salario=0.0):
        self.Nombre = nombre
        self.Edad = edad
        self.Salario = salario

    def clasificacion_edad(self):

        if self.Edad <= 21:
            print("Principiante")

        elif self.Edad < 35:
            print("Senior")

    def aumentar_salario(self, bonificacion):

        self.Salario += self.Salario * bonificacion / 100
        print(f"Aumentado el salario en un {bonificacion}%")

    def __str__(self):

        return f"Nombre: {self.Nombre}" \
               f"\nEdad: {self.Edad}" \
               f"\nSalario: {self.Salario}"


class Programador(Empleado):

    def __init__(self, nombre, edad, salario, lineasDeCodigoPorHora=0, lenguajeDominante=""):
        Empleado.__init__(self, nombre, edad, salario)

        self.LineasDeCodigoPorHora = lineasDeCodigoPorHora
        self.LenguajeDominante = lenguajeDominante

    def __str__(self):
        return f"Nombre: {self.Nombre}" \
               f"\nEdad: {self.Edad}" \
               f"\nSalario: {self.Salario}" \
               f"\nLíneas de código por hora: {self.LineasDeCodigoPorHora}" \
               f"\nLenguaje dominante: {self.LenguajeDominante}"


empleado1 = Empleado("Juan", 19, 950)
empleado2 = Empleado("Ana", 28, 1200.54)

programador1 = Programador("María", 38, 2357.10, 100, "Java")
programador2 = Programador("Pedro", 25, 3841, 250, "Python")

print(empleado1)
empleado1.clasificacion_edad()
empleado1.aumentar_salario(10)
print(empleado1)

print("")

print(programador1)
programador1.clasificacion_edad()
programador1.aumentar_salario(25)
print(programador1)
