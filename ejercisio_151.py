#Ejercisio 151: manipulacion dee datos con pandas.

import pandas as pd

data={
    "Mes":['Enero', 'Febrero', 'Marzo', 'Abril'],
    'ventas':[30500, 35600,28300,33900],
    'Gastos': [22000,23400,18100,20700]
}

df=pd.DataFrame(data)
print(df)