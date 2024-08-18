#Ejercisio 65: Covertir segundos en dias; horas, minutos y segundos.

segundos= int(input('Escriba la cantidad de segundos: '))

dias =segundos //(24*60*60)
segundos = segundos %(24*60*60)
horas = segundos // (60*60)
segundos = segundos %(60*60)
minutos= segundos // (60)
segundos =segundos%60

print ('Dias: {} -Horas: {} -Mnutos: {} -Segundos: {}'.format(dias,horas,minutos, segundos))