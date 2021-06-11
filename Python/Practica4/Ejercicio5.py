billetes = [500, 200, 100, 50, 20, 10, 5, 2, 1]
cantidad_billetes = [0, 0, 0, 0, 0, 0, 0, 0, 0]

cantidad = int(input("Introduzca una cantidad: "))

if cantidad > 0:
    i = 0
    while i <= len(billetes) and cantidad > 0:
        if cantidad >= billetes[i]:
            cantidad_billetes[i] += cantidad // billetes[i]
            cantidad = cantidad % billetes[i]
        i += 1

    for i in range(len(billetes)):
        if cantidad_billetes[i] > 0:
            print(f"{cantidad_billetes[i]} billetes de {billetes[i]}")

else:
    print("Introduzca una cantidad válida")
