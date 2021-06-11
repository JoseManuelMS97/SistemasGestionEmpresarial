class Ccoche:

    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    @staticmethod
    def arrancar_motor():
        print("Arrancando motor...")

    @staticmethod
    def acelerar():
        print("Acelerando")

    @staticmethod
    def subir_marcha():
        print("Subiendo marcha")

    @staticmethod
    def frenar():
        print("Frenando")

    @staticmethod
    def bajar_marcha():
        print("Bajando marcha")

    @staticmethod
    def apagar_motor():
        print("Apagando motor...")


if __name__ == '__main__':
    coche = Ccoche("Honda", "Civic", "Negro")
    coche.arrancar_motor()
    coche.acelerar()
    coche.subir_marcha()
    coche.acelerar()
    coche.subir_marcha()
    coche.frenar()
    coche.bajar_marcha()
    coche.frenar()
    coche.bajar_marcha()
    coche.apagar_motor()