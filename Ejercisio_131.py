#Ejercisio 131: DESEMPAQUETAR UN OPERADOR.

#Dada a una lista con varios elementos, desempaqueta los prmeros dos elementos de las varibles individuaes
#y el resto en una lista separada.

lista=[21,32,45,34,76,89,13.14]

primero, segundo,*resto=lista

print(primero)
print(segundo)
print(resto)