import streamlit as st
import pandas as pd
import numpy as np
import geopandas as gpd
import json

with open('Mapa de Accidentalidad Vial Municipio de Medellín 2016.geojson', "r") as read_file:
    data = json.load(read_file)

st.title("Accidentalidad Municipio de Medellín 2016")

st.write('Se entiende por accidente de tránsito  evento, generalmente involuntario, generado al menos por un un vehículo en movimiento, que causa daños a '
         'personas y bienes involucrados en él, e igualmente afecta la normal circulación de los vehículos que se movilizan por la vía o vías comprendidas en el' 
         'lugar o dentro de la zona de influencia del hecho0 (Ley 769 de 2002 - Código Nacional de Tránsito)'
         )
st.subheader('Sistema de consulta de Accidentalidad municipio de Medellín')

La = []
Lo= []
day=[]
hour=[]
neig=[]
dir=[]    

# Decodificar el archivo en formato JSON (Java Script Object Notation)
for feature in data['features']:
    coordinates = feature['geometry']['coordinates']
    dia=feature['properties']['dia']
    Hora=feature['properties']['hora']
    barrio=feature['properties']['barrio']
    direccion=feature['properties']['direccion']
    La.append(coordinates[1])
    Lo.append(coordinates[0])  
    day.append(dia)
    hour.append(Hora)
    neig.append(barrio)
    dir.append(direccion)
    
nm= st.slider('Selecciona el número de registros de accidentes quieres visualizar', 5, 10000)
#Construir la tabla de datos (dataframe)
dfLa = pd.DataFrame({'lat':La[0 : nm]})
dfLo = pd.DataFrame({'lon':Lo[0 : nm]})
dfdia= pd.DataFrame({'día' :day[0:nm]})
dfhor= pd.DataFrame({'Hora' :hour[0:nm]})
dfbarr=pd.DataFrame({'Barrio':neig[0:nm]})
dfdir=pd.DataFrame({'Dirección':dir[0:nm]})
df_g=pd.concat([dfLa, dfLo, dfdia, dfhor,dfdir,dfbarr], axis=1)

# Mostrar la tabla de datos (dataframe)
st.dataframe(df_g)
#Dibujar el mapa utilizando las columnas 'lat', 'lon'.
st.map(df_g)

# Realizar un filtrado de los datos
st.subheader('Filtrado')

# Primero, selecciona el filtro por día
option_day = st.selectbox('Selecciona filtro por día', ('LUNES', 'MARTES', 'MIÉRCOLES', 'JUEVES', 'VIERNES', 'SÁBADO', 'DOMINGO'))

# Luego, selecciona el filtro por hora mínimo
option_hour_min = st.selectbox('Selecciona filtro por Hora Mínima',
                               ('00:00:00', '01:00:00', '02:00:00', '03:00:00', '04:00:00', '05:00:00',
                                '06:00:00', '07:00:00', '08:00:00', '09:00:00', '10:00:00', '11:00:00',
                                '12:00:00', '13:00:00', '14:00:00', '15:00:00', '16:00:00', '17:00:00',
                                '18:00:00', '19:00:00', '20:00:00', '21:00:00', '22:00:00', '23:00:00'), key='1')

# Luego, selecciona el filtro por hora máximo
option_hour_max = st.selectbox('Selecciona filtro por Hora Máxima',
                               ('00:00:00', '01:00:00', '02:00:00', '03:00:00', '04:00:00', '05:00:00',
                                '06:00:00', '07:00:00', '08:00:00', '09:00:00', '10:00:00', '11:00:00',
                                '12:00:00', '13:00:00', '14:00:00', '15:00:00', '16:00:00', '17:00:00',
                                '18:00:00', '19:00:00', '20:00:00', '21:00:00', '22:00:00', '23:00:00'), key='2')

# Agregar el filtro por barrio
option_neighborhood = st.selectbox('Selecciona filtro por Barrio', sorted(df_g['Barrio'].unique()))

# Aplicar el filtro a los datos
df_filtrado = df_g.query('Barrio == @option_neighborhood and día == @option_day and Hora >= @option_hour_min and Hora <= @option_hour_max')

# Mostrar la tabla de datos filtrada
st.dataframe(df_filtrado)

# Intenta mostrar la cantidad de incidentes dentro del filtro
try:
   st.metric("Cantidad de Incidentes dentro del filtro", df_filtrado.shape[0])
except:
    pass

# Mostrar el mapa con los datos filtrados
st.map(df_filtrado)
#st.write(df)
