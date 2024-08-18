#Ejercisio 43: Encomtrar el nombre del so, el nombre y la version de la plataforma.

import platform
import os

print(os.name)
print(platform.system())
print(platform.release())