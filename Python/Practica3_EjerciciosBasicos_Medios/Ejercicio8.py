# 8.- Escribir un programa que “dibuje” un mes del calendario. El programa recibirá como entrada el
# número de días del mes y el día de la semana del primer día del mes.

num_dias = int(input("Número de dias del mes: "))
dia = int(input("Dia 1 es (0 lunes, 6 domingo): "))

print("L\tM\tX\tJ\tV\tS\tD")
for i in range(dia):
    print("\t", end="")

for i in range(1, 7 - dia + 1):
    print(f"{i}\t", end="")
print()

semana = 0
for i in range(7 - dia + 1, num_dias + 1):
    if semana == 7:
        print()
        semana = 0
    print(f"{i}\t", end="")
    semana += 1