#Notacion 28: usos del mdulo random.

import random

x= random.randint(1,6)
y= random.random()

mi_lista=["piedra","papel", "tijera"]
z= random.choice(mi_lista)

cartas=["1", "2","3","4","5","6","7", "8","9", "J", "K", "Q","A"]
random.shuffle(cartas)

print(cartas)