alumnos = ['Ana', 'Pau', 'Luis', 'Mar', 'Paz']
notas = [10, 5.5, 2.0, 8.5, 7.0]


def muestra_nota_de_alumno(alumnos, notas, alumno_buscado):
    for i in range(len(alumnos)):
        if alumnos[i] == alumno_buscado:
            print(alumno_buscado, notas[i])
            return
    print('El alumno {0} no pertenece al grupo'.format(alumno_buscado))


def anadir_alumno_y_nota(alumnos, notas, alumno, nota):
    alumnos.append(alumno)
    notas.append(nota)


def muestra_alumnos_y_notas(alumnos, notas):
    for i in range(len(alumnos)):
        print(alumnos[i], notas[i])
    return


def aprobados(alumnos, notas):
    for i in range(len(notas)):
        if notas[i] >= 5.0:
            print(alumnos[i])
    return


def num_aprobados(notas):
    contador = 0
    for i in range(len(notas)):
        if notas[i] >= 5.0:
            contador += 1
    print('Hay {0} aprobados.'.format(contador))
    return


def alumnos_con_max_nota(alumnos, notas):
    for i in range(len(notas)):
        if notas[i] == 10.0:
            print(alumnos[i])
    return


def alumnos_nota_supera_media(alumnos, notas):
    suma = 0
    for i in range(len(notas)):
        suma += notas[i]
    media = suma / len(notas)

    for i in range(len(notas)):
        if notas[i] >= media:
            print(alumnos[i])
    return


eleccion = 0
while eleccion != 8:
    print("1) Añadir estudiante y calificación")
    print("2) Mostrar lista de estudiantes con sus calificaciones")
    print("3) Mostrar estudiantes aprobados")
    print("4) Número de aprobados")
    print("5) Estudiantes con máxima nota")
    print("6) Estudiantes con nota mayor o igual a la media")
    print("7) Nota estudiante")
    print("8) Finalizar ejecución del programa")
    print()
    eleccion = int(input("Elija una opcion: "))
    if (eleccion == 1):
        alumno = input("Nombre del alumno nuevo: ")
        nota = float(input("Su nota: "))
        anadir_alumno_y_nota(alumnos, notas, alumno, nota)
    elif (eleccion == 2):
        muestra_alumnos_y_notas(alumnos, notas)
    elif (eleccion == 3):
        aprobados(alumnos, notas)
    elif (eleccion == 4):
        num_aprobados(notas)
    elif (eleccion == 5):
        alumnos_con_max_nota(alumnos, notas)
    elif (eleccion == 6):
        alumnos_nota_supera_media(alumnos, notas)
    elif (eleccion == 7):
        alumno_buscado = input("Nombre del alumno: ")
        muestra_nota_de_alumno(alumnos, notas, alumno_buscado)
    elif (eleccion == 8):
        print("FIN DEL PROGRAMA")
