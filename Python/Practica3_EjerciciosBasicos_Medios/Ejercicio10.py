# 10.- Escribir un programa que tome 100 números aleatorios entre 0 y 99. A continuación debe
# mostrar cuántos números están comprendidos en los intervalos [0-19], [20-39], [40-59], [60-79] y
# [80-99].

import random

veinte = 0
cuarenta= 0
sesenta= 0
ochenta= 0
cien = 0

for i in range(0, 100, 1):
    n = random.randint(0, 99)
    if n <= 19:
        veinte += 1
    elif 19 < n <= 39:
        cuarenta += 1
    elif 39 < n <= 59:
        sesenta += 1
    elif 59 < n <= 79:
        ochenta += 1
    elif n > 79:
        cien += 1

print("[ 0 - 19]: ", veinte)
print("[ 20 - 39]: ", cuarenta)
print("[ 40 - 59]: ", sesenta)
print("[ 60 - 79]: ", ochenta)
print("[ 80 - 99]: ", cien)
print("Total: 100")





