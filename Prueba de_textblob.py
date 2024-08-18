from textblob import TextBlob

text = "Hola, ¿cómo estás?"
blob = TextBlob(text)
print(blob.translate(to='en'))

