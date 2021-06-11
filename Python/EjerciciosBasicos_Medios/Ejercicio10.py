import datetime

try:
    hora = input('Hora: ')
    hora_ = datetime.datetime.strptime(hora, '%H:%M:%S')

    horas = hora_.hour
    minutos = hora_.minute
    segundos = hora_.second

    if horas < 24 and minutos < 60 and segundos < 60:
        if segundos < 59 and segundos >= 0:
            print(horas,":",minutos,":",(segundos + 1))
        else:
            if segundos == 59:
                if minutos == 59:
                    if horas == 23:
                        print("00:00:00")
                    else:
                        print(horas + 1, ": 00: 00")
                else:
                    print(horas,":", minutos + 1, ": 00")
except:
    print("\n La hora es incorrecta...")
