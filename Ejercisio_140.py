#Ejercisio 140: concatenacion de cadenas con args.

def concatenar(*args):
    return"".join(args)

print(concatenar("Hola", " ", "Mundo"))
print(concatenar("python ", "es ","genial"))
