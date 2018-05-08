import numpy as np
import matplotlib.pyplot as plt
import random

def sort_doors():
	x=['goat','goat','car']
	np.random.shuffle(x)
	return x
def choose_door():
	return np.random.randint(3)

def reveal_door(lista,choice):
	n=range(len(lista))
	n.remove(choice)
	for i in n:
		if(lista[i]=='goat'):
			lista[i]='GOAT_MONTY'
			return lista
def finish_game(lista,choice,change):
	if(change==False):
		return lista[choice]
	elif(change==True):
		for i in range(len(lista)):
			if(i!=choice and lista[i]!='GOAT_MONTY'):
				return lista[i]
#Se crean las listas donde se guardaran los resultados de los juegos
cambia=[]
no_cambia=[]

#Se realizan los juegos
for i in range(1000):
	eleccion=choose_door()
	cambia.append(finish_game(reveal_door(sort_doors(),eleccion),eleccion,True))
	no_cambia.append(finish_game(reveal_door(sort_doors(),eleccion),eleccion,False))

#Contadores para saber cuantas veces se gano el juego
n=0
m=0
for i in range(1000):	
	if cambia[i]=='car':
		n+=1
	if no_cambia[i]=='car':
		m+=1

print "Cuando se cambia la eleccion la probabilidad de encontrar el carro es de",n/1000.
print "Cuando no se cambia la eleccion la probabilidad de encontrar el carro es de" ,m/1000.


	
