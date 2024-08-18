#Ejercisio 122: En este proyecto, desrrollare un chatbot que nos pida que le digamos algo y tome eso que le decimos
# y analiza el sentimiento y nos responda cual es el sentimiento.

from textblob import TextBlob

class AnalizadorDeSentimientos:
    def analizar_sentimientos(self, texto):
        analisis=TextBlob(texto)
        
        if analisis.sentiment.polarity>0:
            return "positivo"
        elif analisis.sentiment.polarity==0:
            return "neutral"
        else:
            return "negativo"
        
analizardor=AnalizadorDeSentimientos()
resultado= analizardor.analizar_sentimientos("im fine")
print(resultado)

#este coodigo solo se puede usar en ingles.