#Ejercisio 152: Analisis de datos del titanic.

#cargar datos del titanic(puedes descargar el archivo CSV)

import pandas as pd

titanic_df=pd.read_csv('C:\\Users\\jesus\\OneDrive\\Documentos\\codigos de practica de Angel\\Phyton\\ejercisios\\titanic.csv')
#Mostrar dimenciones del DataFrame
print(titanic_df.shape)
#filtrar datos por pasajero con identificador 148
print(titanic_df.loc[147])
#Filtrar filas pares
print(titanic_df.iloc[::2])
#Ordenar nombres de personas en primera clase.
print(titanic_df[titanic_df['Pclass']==1]['Name'].sort_values())
#calcular porcentaje de supervivencia.
survived_percentage= titanic_df['Survive'].mean()*100
print(f'Porcentaje de supervivencia: {survived_percentage:.2f}%')