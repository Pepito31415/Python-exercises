#Ejercisio 153: Manipulaciom de fechas:



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

import datetime
#Crear una columna de fecha a partir de año, mes y dia.
titanic_df['Fecha']=pd.to_datetime(titanic_df['Year'].astype(str)+'-'+titanic_df['Month'].astype(str)+'-'+titanic_df['Day'].astype(str))
#eliminar filas con fechas no validas
titanic_df.dropna(subset=['Fecha'],inplace=True)
#Ordenar por estaciones contaminantes y fecha
titanic_df.sort_values(by=['Estacion','Fecha'], inplace=True)