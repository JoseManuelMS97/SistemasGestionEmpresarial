#
# Antonio Jose Gomez Gomez
# 12/02/2021

def GenerarCircuito(participantes,long_circuito):	#Genera el circuito
	circuito = []
	aux = "----"
	
	#Añade "----" a todas las posiciones
	for x in range(len(participantes)):
		list_aux=[]
		for i in range(long_circuito):
			list_aux.append(aux)
		circuito.append(list_aux)
	
	#Añade a las primeras posiciones los participantes
	for x in range(len(circuito) ):
		circuito[x][0] = participantes[x]

	#MostrarCircuito(circuito)
	return circuito

def MostrarCircuito(circuito):
	# Muestra el circuito. 
	for x in circuito:
		for i in x:
			print(i, end=" ")
		print()
	print()
	# Falta crear variable que guarde el mensaje y lo retorne

def Carrera(circuito):
	import random
	#array con las posiciones de cada participante
	#Por defecto todos estan en la posicion 0
	posiciones = [0,0,0]	#Aquí se debería crear el array posiciones en base a la longitud de circuito

	ganador = []
	pasos = 1
	pasos_rand = 3

	while ganador == []:
		# contador que señala la posición de los arrays
		cont=0
		aux = random.randint(0,2)	#aquí deberia ser len(circuito) - 1 en vez de 2
		for x in circuito:

			#print("random-->",aux)
			#participante auxiliar guarda el nombre del participante para cambiarlo de posición
			part_aux = x[posiciones[cont ] ]
			x[posiciones[cont] ] = "----" #Cambia la posición donde esta el participante por "----"

			#Cambia la posición del participante actual en el array posiciones
			if aux == cont: 
				if posiciones[cont] + pasos_rand < len(x):
					posiciones[cont] += pasos_rand

				else:
					posiciones[cont] = len(x) -1

			else:
				if posiciones[cont] + pasos < len(x):
					posiciones[cont] += pasos

				else:
					posiciones[cont] = len(x) -1
			#Con la nueva posición modifica el array x
			x[posiciones[cont] ] = part_aux
			circuito[cont] = x	#cambia el array correspondiente del circuito por x
			cont += 1	#cambia al siguiente array
		MostrarCircuito(circuito)

		#comprueba la ultima posición del circuito ( la meta ), si hay alguien lo añade al array ganador
		for x in circuito:
			if x[len(x) -1] != "----":
				ganador.append(x[len(x)-1] )
	return ganador


max_participantes=3
lista_participantes=[]
print("--Introduzca los participantes--\n")

for x in range(max_participantes):
	new_participante = input("Introduzca el nombre del participante {0}: ".format(x+1))
	lista_participantes.append(new_participante)

long_circuito=-1
while long_circuito < 6:
	long_circuito = int(input("Indique la longitud del circuito (mínimo 6): "))

circuito = GenerarCircuito(lista_participantes,long_circuito)
MostrarCircuito(circuito)
ganador = Carrera(circuito)

print("Ganador/es:",ganador)
