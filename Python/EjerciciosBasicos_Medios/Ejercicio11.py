aprobados = 0
suspensos = 0

nota1 = float(input("Nota del alumno 01: "))
if nota1 >= 5:
    aprobados += 1
else:
    suspensos += 1
nota2 = float(input("Nota del alumno 02: "))
if nota2 >= 5:
    aprobados += 1
else:
    suspensos += 1
nota3 = float(input("Nota del alumno 03: "))
if nota3 >= 5:
    aprobados += 1
else:
    suspensos += 1
nota4 = float(input("Nota del alumno 04: "))
if nota4 >= 5:
    aprobados += 1
else:
    suspensos += 1
nota5 = float(input("Nota del alumno 05: "))
if nota5 >= 5:
    aprobados += 1
else:
    suspensos += 1

media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

print("Aprobados: ", aprobados)
print("Suspensos: ", suspensos)
print("Nota media: {0:.2f}".format(media))
