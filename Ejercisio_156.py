#Ejercisio 156: Envar datos multivaluados en un formulario

import requests

form_data={'çolor':['balnco','verde'], 'idiom': 'es'}
resp=requests.post('http://mipagina.xyz/formulario/',data=form_data)