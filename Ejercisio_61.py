#Ejercisio 61: Convertirtodas las unidades de tiempo en segundos.

dias= int(input('Escribe la cantidad de dias: '))
horas= int(input('Escribe la cantidad de horas: '))
minutos= int(input('Escribe la cantidad de minutos: '))
segundos = int(input('Escribe la cantidad de segundos: '))

segundos += dias *24 *60*60
segundos += horas * 60*60
segundos+=  minutos *60

print('La cantidad de segundos es igual: {}'.format(segundos))