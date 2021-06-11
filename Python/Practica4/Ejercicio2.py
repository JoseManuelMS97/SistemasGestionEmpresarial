
lista_paises = ['Francia', 'España', 'Portugal', 'Alemania', 'Suiza', 'Noruega', 'China']
lista_categorias = ['A', 'B', 'C', 'D', 'E', 'F']

categorias = []
paises = []

lista_empleados = [
    [1, 'Jose', 'A', 'España'],
    [2, 'Nacho', 'B', 'Francia'],
    [3, 'Pablo', 'B', 'Alemania'],
    [4, 'Jesus', 'C', 'España']
]

print("Listas")

res = []

for i in range(len(lista_empleados)):
    categorias.append(lista_empleados[i][2])
    paises.append(lista_empleados[i][3])

print("\nPaises:")

for i in range(len(lista_paises)):
    if paises.count(lista_paises[i]) > 0:
        print(f"{lista_paises[i]} : {paises.count(lista_paises[i])} repetido")

print("\nCategorias:")

for i in range(len(lista_categorias)):
    if categorias.count(lista_categorias[i]) > 0:
        print(f"{lista_categorias[i]} : {categorias.count(lista_categorias[i])} repetido")


# DICCIONARIO
categorias = {}
paises = {}

dict_empleados = {
    1: ['Jose', 'A', 'España'],
    2: ['Nacho', 'B', 'Francia'],
    3: ['Pablo', 'B', 'Alemania'],
    4: ['Jesus', 'C', 'España']
}

print("\nDiccionarios")

for i in dict_empleados:
    if (dict_empleados[i])[1] not in categorias:
        categorias[(dict_empleados[i])[1]] = 1
    else:
        categorias[(dict_empleados[i])[1]] += 1

    if (dict_empleados[i])[2] not in paises:
        paises[(dict_empleados[i])[2]] = 1
    else:
        paises[(dict_empleados[i])[2]] += 1


print(f"\nCategorias: {categorias}")
print(f"Paises: {paises}")
print(f"País con mayor número de empleados: {max(paises.values())}")
