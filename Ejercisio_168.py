#Medir el tiempo de ejecucion de una tarea

import time

start_time=time.time()
#realizar una tarea que lleva tiempo
end_time=time.time()
elapsed_time=end_time- start_time
print(f'La tarea {elapsed_time:.2f} segundos.')