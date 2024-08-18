#Notacion 22: expreciones regulares.
import re

texto= """Hola maestro, esta es la cadena 1, como estas mi capitan
esta es la lineab 2 de texto.
Y esta es la linea (3) definitiva mi capitan"""

#resultado=re.search("esta",texto,flages=re.IGNORECASE)
#busca digitos
#resultado= re.findall(r"\d", texto)

#busca todo menos digitos
#resultado= re.findall(r"\D",texto)

#busca expreciones alfanumericas
#resultado= re.findall(r"\w",texto)

#buysca tdod menos expreciones alfa numericas
#resultado= re.findall(r"\W",texto)

#Busca busca espacios  en blanco -> espacios, tabs, saltos de linea
#resultado= re.findall(r"\s",texto)

#busca todo ecepto espacios en blanco, lineas, y tabs
#resultado= re.findall(r"\S",texto)

#busca todo menos saltyos de linea
#resultado= re.findall(r".",texto)

#para buscar saltos de linea
#resultado= re.findall(r"\n",texto)

# \ -> cancelacion de caracteres especiales
#resultado= re.findall(r"\.",texto)

#Armando una cadena que busque un numero, seguido de un punto y un espacio.
#resultado= re.findall(F"\d,\s",texto)

#"^" -> busca el comienzo de una linea. (buscando hola al principio de la linea)
#resultado= re.findall(f"^Hola",texto)

#$-> busca el final de una inea.
#resultado= re.findall(f"capitan$",texto,flags=re.M)

#{n} -> busca una n cantidad de veces el valor de la izquierda (3 numero juntos esta vez)
#resultado= re.findall(r"\d{3}",texto)

#{n,m} -> al menos n, como maximo m
resultado= re.findall(r"\d{2,4}",texto)

print(resultado)