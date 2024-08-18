#ejercisio  93: obtener el valor limite de recurcion.

import sys

def fibonacci(n):
    if n== 0 or n== 1:
        return 1
    else:
        return fibonacci(n- 1) + fibonacci(n - 2)
    
print(sys.getrecursionlimit())

numero= 30

print(fibonacci(numero))