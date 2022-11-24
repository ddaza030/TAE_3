import streamlit  as st
import pandas as pd
import numpy as np
import datetime
from PIL import Image
import pydeck as pdk
import datetime
from ast import literal_eval
import plotly.express as px
from math import floor

#imagenes
image = Image.open('desarrollo2.png')
imag1 = Image.open('Escudo_de_Medellin.png')
#imag2 = Image.open('colision.png')

df = pd.read_csv('conteos.csv',sep = ",", encoding='utf-8')
df2 = pd.read_csv('final_limpio.csv',sep = ",", encoding='utf-8').dropna()
predicciones = pd.read_csv('predicciones.csv',sep = ",", encoding='utf-8')
predicciones['fecha'] = pd.to_datetime(predicciones['fecha'], format='%Y-%m-%d')

def prediccion(fecha_inicial, fecha_final, df):

  minimo = np.datetime64('2021-01-01')
  maximo = np.datetime64('2022-12-31')

  if np.datetime64(fecha_inicial) < minimo:
      return -1
  
  if np.datetime64(fecha_final) > maximo:
      return -1

  mask = (df['fecha'] >= np.datetime64(fecha_inicial)) & (df['fecha'] <= np.datetime64(fecha_final))

  accidentes = df.loc[mask]['prediccion'].sum()
  
  return floor(accidentes)

def time_serie(dataset,name):
    fig = px.line(dataset, x='fecha',y=0,title='Serie de tiempo entre las fechas seleccionadas',labels={'fecha':'Fecha','0':'No. de Accidentes del tipo '+name})
    st.plotly_chart(fig)

def map(barrio_seleccionado):
    cluster = df2.loc[df2['barrio'] == barrio_seleccionado, 'cluster'].iloc[0]
    if cluster == 0:
        layer = pdk.Layer(
            "ScatterplotLayer",
            df[df['barrio'] == barrio_seleccionado],
            pickable=True,
            opacity=0.8,
            stroked=True,
            filled=True,
            radius_scale=6,
            radius_min_pixels=3,
            radius_max_pixels=100,
            line_width_min_pixels=1,
            get_position=['ubicacion_x','ubicacion_y'],
            get_radius="exits_radius",
            get_fill_color=[255,0,0],
            get_line_color=[0, 0, 0],
        )
        view_state = pdk.ViewState(latitude=6.25184, longitude=-75.56359, zoom=11, bearing=0, pitch=0)
        r = pdk.Deck(layers=[layer], initial_view_state=view_state,tooltip={"text": "{fecha_accidente}"})
        return r

    if cluster == 1:
        layer = pdk.Layer(
            "ScatterplotLayer",
            df[df['barrio'] == barrio_seleccionado],
            pickable=True,
            opacity=0.8,
            stroked=True,
            filled=True,
            radius_scale=6,
            radius_min_pixels=3,
            radius_max_pixels=100,
            line_width_min_pixels=1,
            get_position=['ubicacion_x','ubicacion_y'],
            get_radius="exits_radius",
            get_fill_color=[240,248,255],
            get_line_color=[0, 0, 0],
        )
        view_state = pdk.ViewState(latitude=6.25184, longitude=-75.56359, zoom=11, bearing=0, pitch=0)
        r = pdk.Deck(layers=[layer], initial_view_state=view_state,tooltip={"text": "{fecha_accidente}"})
        return r

    if cluster == 2:
        layer = pdk.Layer(
            "ScatterplotLayer",
            df[df['barrio'] == barrio_seleccionado],
            pickable=True,
            opacity=0.8,
            stroked=True,
            filled=True,
            radius_scale=6,
            radius_min_pixels=3,
            radius_max_pixels=100,
            line_width_min_pixels=1,
            get_position=['ubicacion_x','ubicacion_y'],
            get_radius="exits_radius",
            get_fill_color=[0,0,255],
            get_line_color=[0, 0, 0],
        )
        view_state = pdk.ViewState(latitude=6.25184, longitude=-75.56359, zoom=11, bearing=0, pitch=0)
        r = pdk.Deck(layers=[layer], initial_view_state=view_state,tooltip={"text": "{fecha_accidente}"})
        return r

    if cluster == 3:
        layer = pdk.Layer(
            "ScatterplotLayer",
            df[df['barrio'] == barrio_seleccionado],
            pickable=True,
            opacity=0.8,
            stroked=True,
            filled=True,
            radius_scale=6,
            radius_min_pixels=3,
            radius_max_pixels=100,
            line_width_min_pixels=1,
            get_position=['ubicacion_x','ubicacion_y'],
            get_radius="exits_radius",
            get_fill_color=[255,255,0],
            get_line_color=[0, 0, 0],
        )
        view_state = pdk.ViewState(latitude=6.25184, longitude=-75.56359, zoom=11, bearing=0, pitch=0)
        r = pdk.Deck(layers=[layer], initial_view_state=view_state,tooltip={"text": "{fecha_accidente}"})
        return r


    if cluster == 4:
        layer = pdk.Layer(
            "ScatterplotLayer",
            df[df['barrio'] == barrio_seleccionado],
            pickable=True,
            opacity=0.8,
            stroked=True,
            filled=True,
            radius_scale=6,
            radius_min_pixels=3,
            radius_max_pixels=100,
            line_width_min_pixels=1,
            get_position=['ubicacion_x','ubicacion_y'],
            get_radius="exits_radius",
            get_fill_color=[255,0,255],
            get_line_color=[0, 0, 0],
        )
        view_state = pdk.ViewState(latitude=6.25184, longitude=-75.56359, zoom=11, bearing=0, pitch=0)
        r = pdk.Deck(layers=[layer], initial_view_state=view_state,tooltip={"text": "{fecha_accidente}"})
        return r

    if cluster == 5:
        layer = pdk.Layer(
            "ScatterplotLayer",
            df[df['barrio'] == barrio_seleccionado],
            pickable=True,
            opacity=0.8,
            stroked=True,
            filled=True,
            radius_scale=6,
            radius_min_pixels=3,
            radius_max_pixels=100,
            line_width_min_pixels=1,
            get_position=['ubicacion_x','ubicacion_y'],
            get_radius="exits_radius",
            get_fill_color=[0,255,255],
            get_line_color=[0, 0, 0],
        )
        view_state = pdk.ViewState(latitude=6.25184, longitude=-75.56359, zoom=11, bearing=0, pitch=0)
        r = pdk.Deck(layers=[layer], initial_view_state=view_state,tooltip={"text": "{fecha_accidente}"})
        return r
#st.write(df2["LONGITUDE"])
df.style.set_properties(subset=['text'], **{'width': '500px'})
st.set_page_config(layout="wide", page_title="Aplicación web de incidentes viales", page_icon=":taxi:")
st.title('Accidentalidad en la ciudad de Medellín')
st.image(imag1,width=150)

st.markdown('En la siguiente página web se podrá visualizar los datos históricos de accidentalidad por accidente,predecir la accidentalidad por tipo de accidente utilizando una ventana y una resolución temporal definidas por el usuario. Ademas de visualizar una agrupación de los barrios en un mapa. Al seleccionar un barrio se puede visualizar las características del barrio y las del grupo al que pertenece. ')

st.markdown('#### Reporte técnico')
st.markdown('En el siguiente link <link> puede consultar el reporte técnico para entender el desarrollo de la página y de las metodologías usadas.')

st.markdown('#### Video promocional')
st.markdown('En el siguiente link <link> puede observar un video en youtube donde se explica los beneficios de la página web y de cómo utilizarla.')


st.markdown('## Visualización')

st.markdown('En el formulario de abajo seleccione la fecha de inicio, la final y el tipo de accidente para visualizar una ventana de tiempo de los datos históricos')


with st.sidebar:
    
    st.image(image,width=80)
    st.markdown("#### Desarrollado por:")
    st.markdown("- Jose Daniel Bustamante Arango.")
    st.markdown("   jobustamantea@unal.edu.co")
    st.markdown("- Daniel Santiago Cadavid Montoya.")
    st.markdown("   dcadavid@unal.edu.co")
    st.markdown("- Ronald Gabriel Palencia.")
    st.markdown("   ropalencia@unal.edu.co")
    st.markdown("- Marlon Calle Areiza.")
    st.markdown("   mcalle@unal.edu.co")
    st.markdown("- Daniel Daza Macías.")
    st.markdown("   dadazam@unal.edu.co")


fecha_inicio = st.date_input(
    "Fecha de inicio",
    datetime.date(2018, 7, 6))

fecha_final= st.date_input(
    "Fecha final",
    datetime.date(2019, 7, 6))

tipo_accidentes = st.selectbox(
    'Seleccione tipo de accidente',
    ('Caida Ocupante', 'Choque', 'Otro', 'Atropello', 'Volcamiento', 'Incendio'))




if st.button('Visualizar'):
    
    
    mask = (df['fecha'] > str(fecha_inicio)) & (df['fecha'] <= str(fecha_final)) & (df['clase_accidente'] == tipo_accidentes )
    
    accidentes = df.loc[mask][['fecha','fecha_accidente','clase_accidente','barrio','comuna']]
    st.markdown('### Ventana de tiempo')
    st.markdown('Tabla con descripción de los accidentes de tipo \''+tipo_accidentes+'\' entre las fechas seleccionadas')
    st.dataframe(accidentes,width=1000, height=200)
    accidentes = accidentes[['fecha','clase_accidente']].value_counts()
    accidentes = pd.DataFrame(accidentes).reset_index()
    accidentes = accidentes.sort_values(by='fecha',ascending=True)
    
    st.markdown('#### Serie de tiempo entre las fechas seleccionadas:')
    st.write("Ponga el cursor sobre la serie de tiempo (la línea azul), para observar el número accidentes de tipo \'"+tipo_accidentes+"\' que ocurrieron en esa fecha."+
            " También puede hacer zoom dejando presionado click y haciendo un recuadro del tamaño que quiera para visualizar una ventana de tiempo más específica."+
            " Para volver a la escala de la gráfica inicial, presione el boton llamado 'Autoscale' o 'Reset Axes' y para desplazarse por la gráfica haga click en el botón 'Pan' y arrastre la gráfica hacia donde necesite moverse.")

    time_serie(accidentes,tipo_accidentes)

st.markdown('## Predicción de atropellos')

st.write("Rango: Del primero de Enero de 2021 hasta el 31 de Diciembre de 2022.")

fecha_inicio_prediccion = st.date_input(
    "Fecha de inicio",
    datetime.date(2021, 1, 1))

fecha_final_prediccion= st.date_input(
    "Fecha final",
    datetime.date(2021, 1, 1))

if st.button('Predecir'):
    accidentes = prediccion(fecha_inicio_prediccion,fecha_final_prediccion,predicciones)

    if accidentes == -1:
        st.write("Ingrese por favor las fechas dentro del rango establecido")
    else:
        st.write("El número de atropellos para el rango de fechas establecido es de "+str(accidentes))

st.markdown('## Agrupamiento')
st.markdown('En esta sección puede seleccionar algún barrio y ver las características que posee. También se puede observar a qué grupo pertenece. En total hay 6 grupos enumerados del 0 al 5.')

nombre_barrio = st.selectbox(
    'Seleccione el nombre de barrio',
    df2['barrio'])

df_diseno_via_barrio = df2[df2['barrio'] == nombre_barrio]
df_diseno_via_barrio = df_diseno_via_barrio[['Ciclo Ruta',   
'Glorieta', 'Interseccion', 'Lote o Predio', 'Paso Elevado',        
       'Paso Inferior', 'Paso a Nivel', 'Pontón', 'Puente', 'Tramo de via',
       'Tunel', 'Via peatonal']]

st.write(df2)

st.write('### Mapa con todos los accidentes históricos en '+ nombre_barrio)
st.write('En el siguiente mapa puede ver todos los accidentes que han ocurrido en el barrio '+ nombre_barrio +'. Los accidentes están representados por una circulo de un color (el color representa el grupo al que pertenece el barrio), si pone el cursor encima del círculo puede observa la fecha del accidente y la hora en que ocurrio.')
st.write(map(nombre_barrio))
st.markdown('### Características del barrio ' + nombre_barrio)

cluster = df2.loc[df2['barrio'] == nombre_barrio, 'cluster'].iloc[0]

#st.markdown('Este barrio pertenece al grupo '+ str(cluster))

if(cluster == 0):
    numero_muertos = df2.loc[df2['barrio'] == nombre_barrio, 'Con muertos'].iloc[0]
    numero_atropellos = df2.loc[df2['barrio'] == nombre_barrio, 'Atropello'].iloc[0]
    df_diseno_via_barrio = df2[df2['barrio'] == nombre_barrio]
    df_diseno_via_barrio = df_diseno_via_barrio[['Ciclo Ruta',   
'Glorieta', 'Interseccion', 'Lote o Predio', 'Paso Elevado',        
       'Paso Inferior', 'Paso a Nivel', 'Pontón', 'Puente', 'Tramo de via',
       'Tunel', 'Via peatonal']]
    nombre_diseno_via = df_diseno_via_barrio.max().sort_values().index[-1]
    numero_accidentes_diseno_via = df_diseno_via_barrio.max().sort_values()[-1]

    st.write('Se presenta la cantidad de accidentes del barrio por lugar en la vía')

    st.dataframe(df_diseno_via_barrio)
    st.markdown('### Grupo 	\u1F534')
    st.markdown("Este barrio pertenecea al grupo " + str(cluster)+ " el cual es el que menor accidentalidad tomando en cuenta las varibles usadas.")
    st.markdown('### Características')
    st.markdown('- Número de muertos en incidentes viales: ' + str(int(numero_muertos)))
    st.markdown('- Número de atropellos: '+ str(int(numero_atropellos)) )
    st.markdown('- El diseño de vía donde hubo más accidentes es ' + str(nombre_diseno_via) + ' con un total de ' + str(int(numero_accidentes_diseno_via)) + ' accidentes.')

elif(cluster == 1):
    numero_muertos = df2.loc[df2['barrio'] == nombre_barrio, 'Con muertos'].iloc[0]
    numero_atropellos = df2.loc[df2['barrio'] == nombre_barrio, 'Atropello'].iloc[0]
    df_diseno_via_barrio = df2[df2['barrio'] == nombre_barrio]
    df_diseno_via_barrio = df_diseno_via_barrio[['Ciclo Ruta',   
'Glorieta', 'Interseccion', 'Lote o Predio', 'Paso Elevado',        
       'Paso Inferior', 'Paso a Nivel', 'Pontón', 'Puente', 'Tramo de via',
       'Tunel', 'Via peatonal']]
    nombre_diseno_via = df_diseno_via_barrio.max().sort_values().index[-1]
    numero_accidentes_diseno_via = df_diseno_via_barrio.max().sort_values()[-1]

    st.write('Se presenta la cantidad de accidentes del barrio por lugar en la vía')

    st.dataframe(df_diseno_via_barrio) 
    st.markdown('### Grupo 	\U0001f535')
    st.markdown("Este barrio pertenecea al grupo" + str(cluster)+ ", compuesto por los barrios de mayor accidentalidad por atropellos y accidentes ocurridos en intersecciones, lotes o predios.")
    st.markdown('### Características')
    st.markdown('- Número de muertos en incidentes viales: ' + str(int(numero_muertos)))
    st.markdown('- Número de atropellos: '+ str(int(numero_atropellos)) )
    st.markdown('- El diseño de vía donde hubo más accidentes es:' + nombre_barrio)
    st.markdown('- Número de atropellos: '+ str(int(numero_atropellos)) )
    st.markdown('- El diseño de vía donde hubo más accidentes es ' + str(nombre_diseno_via) + ' con un total de ' + str(int(numero_accidentes_diseno_via)) + ' accidentes.')

elif(cluster == 2):
    numero_muertos = df2.loc[df2['barrio'] == nombre_barrio, 'Con muertos'].iloc[0]
    numero_atropellos = df2.loc[df2['barrio'] == nombre_barrio, 'Atropello'].iloc[0]
    df_diseno_via_barrio = df2[df2['barrio'] == nombre_barrio]
    df_diseno_via_barrio = df_diseno_via_barrio[['Ciclo Ruta',   
'Glorieta', 'Interseccion', 'Lote o Predio', 'Paso Elevado',        
       'Paso Inferior', 'Paso a Nivel', 'Pontón', 'Puente', 'Tramo de via',
       'Tunel', 'Via peatonal']]
    nombre_diseno_via = df_diseno_via_barrio.max().sort_values().index[-1]
    numero_accidentes_diseno_via = df_diseno_via_barrio.max().sort_values()[-1]

    st.write('Se presenta la cantidad de accidentes del barrio por lugar en la vía')

    st.dataframe(df_diseno_via_barrio) 
    st.markdown('### Grupo 	\U0001f535')
    st.markdown("Este barrio pertenecea al grupo " + str(cluster)+ " el cual es el tercer menor grupo de accidentalidad tomando en cuenta las varibles usadas.")
    st.markdown('### Características')
    st.markdown('- Número de muertos en incidentes viales: ' + str(int(numero_muertos)))
    st.markdown('- Número de atropellos: '+ str(int(numero_atropellos)) )
    st.markdown('- El diseño de vía donde hubo más accidentes es ' + str(nombre_diseno_via) + ' con un total de ' + str(int(numero_accidentes_diseno_via)) + ' accidentes.')


elif(cluster == 3):
    numero_muertos = df2.loc[df2['barrio'] == nombre_barrio, 'Con muertos'].iloc[0]
    numero_atropellos = df2.loc[df2['barrio'] == nombre_barrio, 'Atropello'].iloc[0]
    df_diseno_via_barrio = df2[df2['barrio'] == nombre_barrio]
    df_diseno_via_barrio = df_diseno_via_barrio[['Ciclo Ruta',   
'Glorieta', 'Interseccion', 'Lote o Predio', 'Paso Elevado',        
       'Paso Inferior', 'Paso a Nivel', 'Pontón', 'Puente', 'Tramo de via',
       'Tunel', 'Via peatonal']]
    nombre_diseno_via = df_diseno_via_barrio.max().sort_values().index[-1]
    numero_accidentes_diseno_via = df_diseno_via_barrio.max().sort_values()[-1]
    
    st.write('Se presenta la cantidad de accidentes del barrio por lugar en la vía')

    st.dataframe(df_diseno_via_barrio) 
    st.markdown('### Grupo 	\U0001f7e1')
    st.markdown("Este barrio pertenece al grupo " + str(cluster)+ " el cual está compuesto por el grupo de barrios cuya accidentalidad es la segunda mayor en comparación a los otros")
    st.markdown('### Características')
    st.markdown('- Número de muertos en incidentes viales: ' + str(int(numero_muertos)))
    st.markdown('- Número de atropellos: '+ str(int(numero_atropellos)) )
    st.markdown('- El diseño de vía donde hubo más accidentes es ' + str(nombre_diseno_via) + ' con un total de ' + str(int(numero_accidentes_diseno_via)) + ' accidentes.')
    
elif(cluster == 4):
    numero_muertos = df2.loc[df2['barrio'] == nombre_barrio, 'Con muertos'].iloc[0]
    numero_atropellos = df2.loc[df2['barrio'] == nombre_barrio, 'Atropello'].iloc[0]
    df_diseno_via_barrio = df2[df2['barrio'] == nombre_barrio]
    df_diseno_via_barrio = df_diseno_via_barrio[['Ciclo Ruta',   
'Glorieta', 'Interseccion', 'Lote o Predio', 'Paso Elevado',        
       'Paso Inferior', 'Paso a Nivel', 'Pontón', 'Puente', 'Tramo de via',
       'Tunel', 'Via peatonal']]
    nombre_diseno_via = df_diseno_via_barrio.max().sort_values().index[-1]
    numero_accidentes_diseno_via = df_diseno_via_barrio.max().sort_values()[-1]
    
    st.write('Se presenta la cantidad de accidentes del barrio por lugar en la vía')

    st.dataframe(df_diseno_via_barrio) 
    st.markdown('### Grupo 	\u1F7E3')
    st.markdown("Este barrio pertenece a el grupo " + str(cluster)+ " el cual es el grupo de barrios con menor accidentalidad en todas las variables.")
    st.markdown('### Características')
    st.markdown('- Número de muertos en incidentes viales: ' + str(int(numero_muertos)))
    st.markdown('- Número de atropellos: '+ str(int(numero_atropellos)) )
    st.markdown('- El diseño de vía donde hubo más accidentes es ' + str(nombre_diseno_via) + ' con un total de ' + str(int(numero_accidentes_diseno_via)) + ' accidentes.')

elif(cluster == 5):
    numero_muertos = df2.loc[df2['barrio'] == nombre_barrio, 'Con muertos'].iloc[0]
    numero_atropellos = df2.loc[df2['barrio'] == nombre_barrio, 'Atropello'].iloc[0]
    df_diseno_via_barrio = df2[df2['barrio'] == nombre_barrio]
    df_diseno_via_barrio = df2[df2['barrio'] == nombre_barrio]
    df_diseno_via_barrio = df_diseno_via_barrio[['Ciclo Ruta',   
'Glorieta', 'Interseccion', 'Lote o Predio', 'Paso Elevado',        
       'Paso Inferior', 'Paso a Nivel', 'Pontón', 'Puente', 'Tramo de via',
       'Tunel', 'Via peatonal']]
    nombre_diseno_via = df_diseno_via_barrio.max().sort_values().index[-1]
    numero_accidentes_diseno_via = df_diseno_via_barrio.max().sort_values()[-1]
    
    st.write('Se presenta la cantidad de accidentes del barrio por lugar en la vía')

    st.dataframe(df_diseno_via_barrio) 
    st.markdown("Este barrio pertenecea al grupo " + str(cluster)+ " el cual es el tercer mayor en cuanto a accidentalidad.")
    st.markdown('### Características')
    st.markdown('- Número de muertos en incidentes viales: ' + str(int(numero_muertos)))
    st.markdown('- Número de atropellos: '+ str(int(numero_atropellos)) )
    st.markdown('- El diseño de vía donde hubo más accidentes es ' + str(nombre_diseno_via) + ' con un total de ' + str(int(numero_accidentes_diseno_via)) + ' accidentes.')
    
