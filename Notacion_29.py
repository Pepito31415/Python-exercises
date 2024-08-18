#Notacio 29: manejo de escepciones en python.

try:
    numerador= int(input("ingrese un Numero: "))
    denominador= int(input("ingrese un Numero: "))
    resultado= numerador/ denominador
except ZeroDivisionError as e:
    print(e)
    print("no puedes dividir por cero")
except ValueError as e:
    print(e)
    print("no puede poner caracteres")

except Exception as e:
    print(e)
    print(" Algo salio mal!")
else:
    print(resultado)
finally:
    print("Esto se ejecutara siempre!")