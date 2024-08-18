#Ejercisio 59: Calcular la estructura (dada de pies y pulgadas) en centimetros.

#1 ft= 30.48 cm
#1"=2.54 cm

print('escribe su estatura(ft y pulgadas): ')
pies=float(input('PIes: '))
pulgadas=float(input('Pulgadas: '))

cm= pies* 30.48
cm+=pulgadas+ 2.54

print(' Su estructura {} cm'.format(cm))