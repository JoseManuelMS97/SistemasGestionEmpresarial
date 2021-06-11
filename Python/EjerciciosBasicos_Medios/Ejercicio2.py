deposito = int(input("Tamaño del depósito (litros): "))
combustible = int(input("% de combustible: "))
consumo = int(input("Consumo (1/100 Km): "))

km = combustible * deposito / 100 * consumo

if km>=200:
    print("Puedes recorrer ",km," Km más.")
    print("Espera a la siguiente gasolinera.")
else:
    print("Lo siento, no vas a poder llegar a la gasolinera.")

