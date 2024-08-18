#Ejercisio 164: Crear un directorio temporal

import os
import tempfile
with tempfile.TemporaryDirectory() as temp_dir:
    print(f'Directorio temporal creado: {temp_dir}')