class Banco:

    def __init__(self, saldo, tipo="", puntos=0, cliente=list()):
        self.Saldo = saldo
        self.Cliente = cliente
        self.Interes_Cuenta = 0
        self.Tipo = tipo
        self.Cuenta_Bloqueada = False
        self.Puntos = puntos

        if self.Tipo == "CC":
            self.Interes_Cuenta = 0.1

        elif self.Tipo == "CV":
            self.Interes_Cuenta = 0.2

        elif self.Tipo == "FI":
            self.Interes_Cuenta = 0.34

    def ingresar_dinero(self, cantidad):

        if cantidad > 0:
            self.Saldo += cantidad
            self.Puntos += 1

    def sacar_dinero(self, cantidad):

        if self.Tipo == "CC":

            if self.Saldo >= cantidad:
                self.Saldo -= cantidad

            else:
                print("No te queda tanto dinero en cuenta")

        elif self.Tipo == "FI":

            if self.Saldo > -500 and not self.Cuenta_Bloqueada:
                self.Saldo -= cantidad

                if self.Saldo < -500:
                    self.Cuenta_Bloqueada = True
                    print("Cuenta bloqueada")

            else:
                print("Cuenta bloqueada")

        elif self.Tipo == "CV":

            print("No se puede sacar dinero")

    def consultar_saldo(self):

        return f"{self.Saldo}"

    def cambiar_cliente(self, dni, nombre, apellidos, direccion="", telefono=0):

        self.Cliente = [dni, nombre, apellidos, direccion, telefono]

    def revision_mensual(self, comision=0.6):

        if self.Tipo == "CV":
            pass
        else:
            self.Saldo = self.Saldo + self.Interes_Cuenta - comision

    def __str__(self):
        return f"{self.Cliente} - Puntos: {self.Puntos}"


class Cliente(Banco):

    def __init__(self, dni, nombre, apellidos, direccion="", telefono=0, saldo=0, cliente=list()):
        Banco.__init__(self, saldo, cliente)

        self.Dni = dni
        self.Nombre = nombre
        self.Apellidos = apellidos
        self.Direccion = direccion
        self.Telefono = telefono

    def __str__(self):
        return f"{self.Nombre} {self.Apellidos} - {self.Direccion} - {self.Telefono}"


clientes = list()
cuentas = list()

clientes.append(Cliente("12345678Q", "nombre", "apellidos"))
cuentas.append(Banco(100, "CV", 0, clientes[0]))

cuentas[0].ingresar_dinero(200)
print(cuentas[0].consultar_saldo())

cuentas[0].sacar_dinero(1578)
print(cuentas[0].consultar_saldo())

cuentas[0].cambiar_cliente("0000000", "nombre nuevo", "apellido nuevo", "C/ Invent", 65465456)
print(cuentas[0])

cuentas[0].revision_mensual()
print(cuentas[0].consultar_saldo())
