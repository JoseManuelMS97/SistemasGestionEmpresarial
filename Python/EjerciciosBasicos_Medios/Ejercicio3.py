nota = float(input("Introduzca la nota del alumno: "))

if 0 < nota < 5:
    print("Suspenso")
elif 5 < nota < 6:
    print("Suficiente")
elif 6 < nota < 7:
    print("Bien")
elif 7 < nota < 9:
    print("Notable")
elif 9 < nota < 10:
    print("Sobresaliente")
else:
    print("Ninguna opción válida seleccionada")
