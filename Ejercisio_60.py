#Ejercisio 60: calcularla hpotenusa de un triangulo.

from math import sqrt

ab= float(input('Escribe el valor de la longitut de A yB: '))
bc = float(input('Escribe el valor de la longitud de B y C: '))

hipotenusa = sqrt(ab**2+bc**2)

print('La longitud de la hipotenusa es {}'.format(hipotenusa))