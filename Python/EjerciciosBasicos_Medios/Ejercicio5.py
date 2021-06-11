trabajados = int(input("Días trabajados: "))
festivos = int(input("Días festivos trabajados: "))
turno = input("Turno: (M-Mañana, T-Tarde, N-Noche): ")

sueldo = ((12 * 8) * trabajados) + ((24 * 8) * festivos)
if turno == 'N':
    sueldo += (sueldo * 20) / 100

if trabajados > 30:
        print("Lo siento, no puede ser mayor a 30 días.")
else:
    print("Sueldo: ", sueldo, " euros.")
