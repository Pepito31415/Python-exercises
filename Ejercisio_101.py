#Ejercisio 101: formatear la sqalida de una caddena de caracteres.

x=2
y=3
suma= x+y

print('La suma de '+str(x)+' y ' + str(y) +' es igual a ' + str(suma))
print('la suma de ',x,' y ', y,' es igual a ',str(suma))
print('la suma de %d y %d es igual a %d' % (x, y, suma))
print('la suma de {} y {} es igual a {}'.format(x, y, suma))
print(f'la suma de {x} y {y} es igual a {suma}')