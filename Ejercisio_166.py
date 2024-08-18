#Ejercisio 166: Obtener la hora actual en un formato.

import time
current_time= time.localtime()
formatted_time= time.strftime("%H:%M:%S", current_time)
print("Hora actual (formato 24 horas):", formatted_time)