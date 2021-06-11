
import random

palabras = {
    1: "PROGRAMACIÓN",
    2: "MOVIL",
    3: "GAFAS",
    4: "BOTELLA",
    5: "MESA",
    6: "RATON",
    7: "PANTALLA",
    8: "INTERNET",
    9: "ROUTER",
    10: "TECLADO",
    11: "MANDO",
    12: "SILLA",
    13: "ESCRITORIO",
    14: "BANCO",
    15: "USB",
    16: "ALTAVOZ",
    17: "PROYECTOR",
    18: "TRIPODE",
    19: "PERRO",
    20: "CAMISETA"
}

n_intentos = 0
letras_jugadas = 0
letras_int = set()

palabra = random.randint(1, 20)
shadow = ["_"] * len(palabras[palabra])
print(palabras[palabra])


def draw():
    int1 = f"-------------|\n" \
           f"|\n" \
           f"|\n" \
           f"|\n" \
           f"|                  {shadow}\n" \
           f"|\n" \
           f"|\n" \
           f"|\n" \
           f"|\n" \
           f"|\n" \
           f"---\n" \
           f"Letras jugadas: {letras_jugadas} ({letras_int})\n" \
           f"Diga una letra: _\n"

    int2 = f"-------------|\n" \
           f"|           ###\n" \
           f"|           ###\n" \
           f"|            |\n" \
           f"|            |      {shadow}\n" \
           f"|            |\n" \
           f"|\n" \
           f"|\n" \
           f"|\n" \
           f"|\n" \
           f"---\n" \
           f"Letras jugadas: {letras_jugadas} ({letras_int})\n" \
           f"Diga una letra: _\n"

    int3 = f"-------------|\n" \
           f"|           ###\n" \
           f"|           ###\n" \
           f"|            |\n" \
           f"|            |      {shadow}\n" \
           f"|        ----|\n" \
           f"|\n" \
           f"|\n" \
           f"|\n" \
           f"|\n" \
           f"---\n" \
           f"Letras jugadas: {letras_jugadas} ({letras_int})\n" \
           f"Diga una letra: _\n"

    int4 = f"-------------|\n" \
           f"|           ###\n" \
           f"|           ###\n" \
           f"|            |\n" \
           f"|            |      {shadow}\n" \
           f"|        ----|----\n" \
           f"|\n" \
           f"|\n" \
           f"|\n" \
           f"|\n" \
           f"---\n" \
           f"Letras jugadas: {letras_jugadas} ({letras_int})\n" \
           f"Diga una letra: _\n"

    int5 = f"-------------|\n" \
           f"|           ###\n" \
           f"|           ###\n" \
           f"|            |\n" \
           f"|            |      {shadow}\n" \
           f"|        ----|----\n" \
           f"|           /\n" \
           f"|          /\n" \
           f"|         /\n" \
           f"|\n" \
           f"---\n" \
           f"Letras jugadas: {letras_jugadas} ({letras_int})\n" \
           f"Diga una letra: _\n"

    int6 = f"-------------|\n" \
           f"|           ###\n" \
           f"|           ###\n" \
           f"|            |\n" \
           f"|            |      {shadow}\n" \
           f"|        ----|----\n" \
           f"|           / \\\n" \
           f"|          /   \\\n" \
           f"|         /     \\\n" \
           f"|\n" \
           f"---\n" \
           f"Letras jugadas: {letras_jugadas} ({letras_int})\n" \
           f"Diga una letra: _\n"
    screens = [int1, int2, int3, int4, int5, int6]
    return screens[screen_counter]


acierto = False
screen_counter = 0
while not acierto and n_intentos < 6:
    letra = input(draw()).upper()
    letras_jugadas += 1
    if letra in palabras[palabra] and letra not in letras_int:
        for i in range(len(palabras[palabra])):
            if letra == palabras[palabra][i]:
                shadow[i] = letra
    else:
        screen_counter += 1
        n_intentos += 1
        letras_int.add(letra)
    if shadow.count("_") == 0:
        print(draw())
        continuar = input(f"Has acertado la palabra: {palabras[palabra]}, quieres continuar? S/N").upper()
        if continuar == "N":
            acierto = True
        else:
            n_intentos = 0
            letras_int = set()
            palabra = random.randint(1, 20)
            letras_jugadas = 0
            shadow = ["_"] * len(palabras[palabra])

if not acierto:
    print("Has perdido")