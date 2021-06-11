total = int(input("Importe total: "))
descuento = 0
ahorrado = 0

if total > 20:
    descuento = 20
else:
    descuento = 10

ahorrado = (total * descuento) / 100
final = total - ahorrado
print("Descuento: ", ahorrado, "€ (", descuento, "%)")
print("Importe tras descuento: ", final, "€")
