# 3.- Programa que lee notas de los alumnos y dice cuántos están aprobados y cuál es la nota
# media. El programa dejará de pedir notas, cuando se pulse la tecla ENTER.

print("Introduzca las notas, ENTER para terminar:")
i = 0
nota = 1
notas = 0
aprobados = 0
suspensos = 0

nota = input("Nota del alumno :")

while not (str(nota) == ""):
    notas += float(nota)
    if float(nota) >= 5:
        aprobados += 1
    else:
        suspensos += 1
    i += 1
    nota = input("Nota del alumno :")

print("Número de alumnos: ", i)
print("Aprobados: ", aprobados)
print("Suspensos: ", suspensos)
print("Nota media: ", notas / i)
