#Ejercisio 137: verificacion de palindromo usando funciones anidadas:

def es_palindromo(palabra):
    def limpiar_texto(texto):
        return texto.replace(" "," ").lower()
    
    palabra_limpia= limpiar_texto(palabra)
    return palabra_limpia== palabra_limpia[::-1]

print(es_palindromo("Anita lava la tina"))
print(es_palindromo("Hola mundo"))