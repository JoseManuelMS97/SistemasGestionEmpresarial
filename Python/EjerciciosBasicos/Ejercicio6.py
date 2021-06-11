num = int(input("Dame un numero de dos cifras: "))

if num < 10 or num > 99:
    print("Lo siento, el número ", num ," no me sirve, debe  de ser de 2 cifras.")
else:
    num = str(num)
    print("El número al revés es: "+(num[::-1]))