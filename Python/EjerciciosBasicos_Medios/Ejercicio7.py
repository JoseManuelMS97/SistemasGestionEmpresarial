from datetime import datetime

mesesDic = {
    "01": 'Enero',
    "02": 'Febrero',
    "03": 'Marzo',
    "04": 'Abril',
    "05": 'Mayo',
    "06": 'Junio',
    "07": 'Julio',
    "08": 'Agosto',
    "09": 'Septiembre',
    "10": 'Octubre',
    "11": 'Noviembre',
    "12": 'Diciembre'
}


def comprobar_fecha():
    try:
        fecha_str = input('\n Ingrese fecha "dd/mm/aaaa"...: ')
        fecha = datetime.strptime(fecha_str, '%d/%m/%Y')
        day = fecha.day
        month = fecha.month
        mes = mesesDic[str(month)]
        year = fecha.year
        print("La fecha es {} de {} de {}".format(day, mes, year))
    except:
        print("\n La fecha es incorrecta...")


comprobar_fecha()
