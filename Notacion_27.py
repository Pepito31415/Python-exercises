#Notacion 27: metodo format.

str_1="leche"
str_2="casar"

# print("Arroz con leche me quiero casar")
# print("Arroz con "+str_1+" me quiero "+str_2)
print("Arros con {} me quiero {}".format(str_1, str_2))
print("Arros con {} me quiero {}".format("leche","casar"))
print("Arros con {1} me quiero {0}".format(str_1, str_2))
print("Arros con {str_1} me quiero {str_2}".format(str_1= "leche", str_2= "casar"))
print("Arros con {str_1} me quiero {str_2}".format(str_1= str_1, str_2= str_2))

texto="Arros con {} me quiero {}"
print(texto.format(str_1, str_2))