frase = input("Introduzca una frase: ").lower()

letras = {}

for i in frase.replace(" ", ""):
    if i not in letras:
        letras[i] = 1
    else:
        letras[i] += 1

print(letras)