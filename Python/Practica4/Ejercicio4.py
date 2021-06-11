nombres = []
nombre = input("Introduce nombres. ENTER para terminar\n")

while nombre != "":
    nombres.append(nombre)
    nombre = input()

if len(nombres) > 0:
    nombres.sort()

    print("Los nombres son: ")
    for i in nombres:
        print(i)
else:
    print("No ha introducido ningún nombre")