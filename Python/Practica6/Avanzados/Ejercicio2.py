class Empleado:
    def __init__(self, nombre="", edad=0, salario=0.0):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def __str__(self):
        return f"Nombre: {self.nombre} \nEdad: {self.edad} \nSalario: {self.salario}"

    def clas_segun_edad(self):
        if self.edad <= 21:
            print("Principiante.")
        elif 22 <= self.edad < 35:
            print("Senior.")

    def aumentar_salario(self, porcentaje):
        self.salario += (self.salario * porcentaje) / 100

class Programador(Empleado):
    def __init__(self, nombre="", edad=0, salario=0.0, lineasDeCodigoPorHora=0, lenguajeDominante=""):
        Empleado.__init__(self, nombre, edad, salario)
        self.lineasDeCodigoPorHora = lineasDeCodigoPorHora
        self.lenguajeDominante = lenguajeDominante

    def __str__(self):
        return f"Nombre: {self.nombre} \nEdad: {self.edad} \nSalario: {self.salario} \nLineasDeCodigoPorHora: {self.lineasDeCodigoPorHora} \nLenguajeDominante: {self.lenguajeDominante}"


if __name__ == '__main__':
    empleados = []
    eleccion = 0
    while eleccion != 4:
        print("1) Crear Empleado.")
        print("2) Crear Programador.")
        print("3) Aumentar sueldo.")
        print("4) Finalizar ejecución del programa")
        print()
        eleccion = int(input("Elija una opcion: "))

        if (eleccion == 1):
            nombre = input("Nombre del empleado: ")
            edad = int(input("Edad del empleado: "))
            salario = float(input("Salario del empleado: "))

            empleado = Empleado(nombre,edad,salario)
            empleados.append(empleado)

        elif (eleccion == 2):
            nombre = input("Nombre del empleado: ")
            edad = int(input("Edad del empleado: "))
            salario = float(input("Salario del empleado: "))
            lineashora = int(input("Lineas por hora: "))
            ldominante = input("Lenguaje dominante: ")

            programador = Programador(nombre, edad, salario,lineashora,ldominante)
            empleados.append(programador)

        elif (eleccion == 3):
            porcentaje = float(input("Que porcentaje quiere subirles el sueldo?: "))
            for e in empleados:
                e.aumentar_salario(porcentaje)

        elif (eleccion == 4):
            print("FIN DEL PROGRAMA")
