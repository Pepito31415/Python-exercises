#Ejercisio 57: Medir el tienmpo de ejecucion de un metodo.

import time

def sumar_range(n):
    t_0=time.time()

    suma=0

    for i in range(1, n+1):
        suma+=i

    t_1 =time.time()

    return suma, t_1-t_0

n=100000

print(sumar_range(n))

n=10000000

print(sumar_range(n))