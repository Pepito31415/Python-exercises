#Ejercisio 155: Hacer una peticio POST.

import requests

auth_data={'email':'juanjo@j2logo.com','pass': '1234'}

requests.post('http://mipagina.xyz/login/', data=auth_data)