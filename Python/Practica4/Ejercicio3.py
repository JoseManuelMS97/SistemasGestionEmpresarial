num_alumnos = 0
num_aprobados = 0
notas = []

print("Introduzca las notas, ENTER para terminar ")
nota = input(f"Nota del alumno {num_alumnos + 1}: ")


while nota != "":
    notas.append(float(nota))
    num_alumnos += 1

    if float(nota) >= 5:
        num_aprobados += 1

    nota = input(f"Nota del alumno {num_alumnos + 1}: ")

if num_alumnos > 0:
    print("Se han introducido las siguientes notas:")
    for i in range(len(notas)):
        print(f"\tAlumno {i + 1}: {notas[i]}")

    print(f"Resumen: ")
    print(f"\tNumero de alumnos: {num_alumnos}")
    print(f"\tAprobados: {num_aprobados}")
    print(f"\tSuspensos: {len(notas) - num_aprobados}")
    print(f"\tNota media: {sum(notas) / (len(notas))}")
else:
    print("No se ha introducido ningún alumno")