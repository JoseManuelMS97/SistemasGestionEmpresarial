origen = input("Me falla el GPS, ¿dónde estamos? ")
destino = input("¿A dónde vamos? ")
velocidad = int(input("¿A qué velocidad? "))
distancia = int(input("¿Te sabes la distancia? "))

tiempo = distancia/velocidad
tiempo2 = distancia/120

print("A",velocidad,"Km/h tardaríamos ",tiempo," horas")
print("A 120 Km/h tardaríamos ",round(tiempo2,2)," horas, pero mejor no correr mucho :) ")

