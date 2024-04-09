import streamlit as st
import pandas as pd
import json

with open('Mapa de Accidentalidad Vial Municipio de Medellín 2016.geojson', "r") as read_file:
    data = json.load(read_file)

st.title("Accidentalidad Municipio de Medellín 2016")

st.image("Accidentes.jpg")

st.write('Se entiende por accidente de tránsito un evento, generalmente involuntario, generado al menos por un vehículo en movimiento, que causa daños a '
         'personas y bienes involucrados en él, e igualmente afecta la normal circulación de los vehículos que se movilizan por la vía o vías comprendidas en el' 
         'lugar o dentro de la zona de influencia del hecho (Ley 769 de 2002 - Código Nacional de Tránsito)'
         )

st.subheader('Sistema de consulta de Accidentalidad municipio de Medellín')

La = []
Lo = []
day = []
hour = []
neig = []
dir = []
accident_type = []
severity = []

# Decodificar el archivo en formato JSON
for feature in data['features']:
    coordinates = feature['geometry']['coordinates']
    dia = feature['properties']['dia']
    Hora = feature['properties']['hora']
    barrio = feature['properties']['barrio']
    direccion = feature['properties']['direccion']
    tipo_accidente = feature['properties']['tipo_accidente']
    gravedad = feature['properties']['gravedad']
    La.append(coordinates[1])
    Lo.append(coordinates[0])
    day.append(dia)
    hour.append(Hora)
    neig.append(barrio)
    dir.append(direccion)
    accident_type.append(tipo_accidente)
    severity.append(gravedad)

# Construir el DataFrame
df_g = pd.DataFrame({'lat': La, 'lon': Lo, 'día': day, 'Hora': hour, 'Dirección': dir, 'Barrio': neig,
                     'Tipo de Accidente': accident_type, 'Gravedad': severity})

# Filtros
st.subheader('Filtrado')

# Filtro por día
option_day = st.selectbox('Selecciona filtro por día', ('LUNES', 'MARTES', 'MIÉRCOLES', 'JUEVES', 'VIERNES', 'SÁBADO', 'DOMINGO'))

# Filtro por hora mínimo
option_hour_min = st.selectbox('Selecciona filtro por Hora Mínima',
                               ('00:00:00', '01:00:00', '02:00:00', '03:00:00', '04:00:00', '05:00:00',
                                '06:00:00', '07:00:00', '08:00:00', '09:00:00', '10:00:00', '11:00:00',
                                '12:00:00', '13:00:00', '14:00:00', '15:00:00', '16:00:00', '17:00:00',
                                '18:00:00', '19:00:00', '20:00:00', '21:00:00', '22:00:00', '23:00:00'), key='1')

# Filtro por hora máximo
option_hour_max = st.selectbox('Selecciona filtro por Hora Máxima',
                               ('00:00:00', '01:00:00', '02:00:00', '03:00:00', '04:00:00', '05:00:00',
                                '06:00:00', '07:00:00', '08:00:00', '09:00:00', '10:00:00', '11:00:00',
                                '12:00:00', '13:00:00', '14:00:00', '15:00:00', '16:00:00', '17:00:00',
                                '18:00:00', '19:00:00', '20:00:00', '21:00:00', '22:00:00', '23:00:00'), key='2')

# Filtro por barrio
#option_neighborhood = st.selectbox('Selecciona filtro por Barrio', sorted(df_g['Barrio'].unique()))

# Filtro por tipo de accidente
#option_accident_type = st.multiselect('Selecciona filtro por Tipo de Accidente', sorted(df_g['Tipo de Accidente'].unique()))

# Filtro por gravedad del accidente
#option_severity = st.multiselect('Selecciona filtro por Gravedad del Accidente', sorted(df_g['Gravedad'].unique()))

# Aplicar los filtros
#df_filtrado = df_g.query('Barrio == @option_neighborhood and día == @option_day and Hora >= @option_hour_min and Hora <= @option_hour_max and \
#                         `Tipo de Accidente` in @option_accident_type and Gravedad in @option_severity')

# Mostrar la tabla de datos filtrados
st.dataframe(df_filtrado)

# Mostrar la cantidad de incidentes dentro del filtro
st.metric("Cantidad de Incidentes dentro del filtro", df_filtrado.shape[0])

# Mostrar el mapa con los datos filtrados
st.map(df_filtrado)

# Mostrar el mapa con los datos filtrados
st.map(df_filtrado)
#st.write(df)
