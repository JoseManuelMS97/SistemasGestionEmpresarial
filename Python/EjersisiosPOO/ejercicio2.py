
# Nombre: Nacho Riquelme
# Fecha: 6/2/21
# Ejercicio 2: Cree una clase Ccoche que represente coches.

class Ccoche:

    def __init__(self, marca, modelo, color, acelerar=0, estado_motor=False, marcha=0):

        self.CMarca = marca
        self.CModelo = modelo
        self.CColor = color
        self.CAcelerar = acelerar
        self.CEstado_motor = estado_motor
        self.CMarcha = marcha

    def arrancar_motor(self):

        if self.CEstado_motor:
            print("El motor está en marcha")

        else:
            self.CEstado_motor = True
            print("Encendiendo motor...")

    def apagar_motor(self):

        if not self.CEstado_motor:
            print("El motor está apagado")

        else:
            self.CEstado_motor = False
            print("Apagando motor...")

    def subir_marcha(self):

        if self.CMarcha == 5:
            print("El coche es de 5 velocidades. No puedes subir más marchas")

        else:
            self.CMarcha += 1
            print(f"Introduciendo marcha {self.CMarcha}")

    def bajar_marcha(self):

        if self.CMarcha == 1:
            print("Estás en la primera marcha. No puedes bajar más.")

        else:
            self.CMarcha -= 1
            print(f"Introduciendo marcha {self.CMarcha}")

    def acelerar(self):

        if self.CMarcha == 120:
            print("Vas a la máxima velocidad. No puedes acelerar más")

        else:
            self.CAcelerar += 10
            print(f"El coche va a {self.CAcelerar} km/h")

    def frenar(self):

        if self.CMarcha == 10:
            print("No puedes seguir frenando o se apagará el motor.")

        else:
            self.CAcelerar -= 10
            print(f"El coche va a {self.CAcelerar} km/h")


coche = Ccoche("Volvo", "S40", "Blanco")

coche.arrancar_motor()
coche.acelerar()
coche.subir_marcha()
coche.acelerar()
coche.subir_marcha()
coche.frenar()
coche.bajar_marcha()
coche.apagar_motor()