import streamlit  as st
import pandas as pd
import numpy as np
import datetime
from PIL import Image
import pydeck as pdk
import datetime
from ast import literal_eval
import plotly.express as px

#imagenes
image = Image.open('desarrollo2.png')
imag1 = Image.open('Escudo_de_Medellin.png')

df = pd.read_csv('conteos.csv',sep = ",", encoding='utf-8')
df2 = pd.read_csv('final.csv',sep = ",", encoding='utf-8').dropna()

def time_serie(dataset,name):
    #fig = go.Figure()
    #fig.add_trace(go.Scatter(x=conteos['fecha_accidente'],y=conteos['0']))
    #fig.show()
    fig = px.line(dataset, x='fecha',y=0,title='Seri de tiempo entre las fechas seleccionadas')
    st.plotly_chart(fig)

def map(barrio_seleccionado):
    
    layer = pdk.Layer(
        "ScatterplotLayer",
        df[df['barrio'] == barrio_seleccionado],
        pickable=True,
        opacity=0.8,
        stroked=True,
        filled=True,
        radius_scale=6,
        radius_min_pixels=1,
        radius_max_pixels=100,
        line_width_min_pixels=1,
        get_position=['ubicacion_x','ubicacion_y'],
        get_radius="exits_radius",
        get_fill_color=[255, 140, 0],
        get_line_color=[0, 0, 0],
    )

    # Set the viewport location
    view_state = pdk.ViewState(latitude=6.557998, longitude=-75.545921, zoom=1, bearing=0, pitch=0)

    # Render
    r = pdk.Deck(layers=[layer], initial_view_state=view_state)
    return r


#st.write(df2["LONGITUDE"])
df.style.set_properties(subset=['text'], **{'width': '500px'})
st.set_page_config(layout="wide", page_title="Aplicación web de clusters", page_icon=":taxi:")
st.title('Accidentalidad en la ciudad de Medellín')
st.image(imag1,width=150)
st.markdown('En la siguiente página web se podrá visualizar los datos históricos de accidentalidad por accidente,predecir la accidentalidad por tipo de accidente utilizando una ventana y una resolución temporal definidas por el usuario y visualizar los grupos de barrios en un mapa. Al seleccionar un barrio se deben poder visualizar las características del barrio y las del grupo al que pertenece. ')

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
    "fecha de inicio",
    datetime.date(2019, 7, 6))

fecha_final= st.date_input(
    "fecha final",
    datetime.date(2019, 7, 6))

tipo_accidentes = st.selectbox(
    'Seleccione tipo de accidente',
    ('Caida Ocupante', 'Choque', 'Otro', 'Atropello', 'Volcamiento',
       'Caída de Ocupante', 'Incendio'))




if st.button('calcular'):
    
    
    mask = (df['fecha'] > str(fecha_inicio)) & (df['fecha'] <= str(fecha_final)) & (df['clase_accidente'] == tipo_accidentes )
    
    st.write(tipo_accidentes)
    accidentes = df.loc[mask][['fecha','fecha_accidente','clase_accidente','barrio','comuna']]
    st.markdown('### Ventana de tiempo')
    st.markdown('Tabla con descripción de los accidentes entre las fechas seleccionadas')
    st.dataframe(accidentes,width=1000, height=200)
    accidentes = accidentes[['fecha','clase_accidente']].value_counts()
    accidentes = pd.DataFrame(accidentes).reset_index()
    accidentes = accidentes.sort_values(by='fecha',ascending=True)
    
    st.markdown('#### Serie de tiempo entre las fechas seleccionadas')
    st.write("Ponga el cursor sobre la serie de tiempo (la línea azul), para observar el número de tipos de accidentes seleccionados que ocurrieron en esa fecha.")

    time_serie(accidentes,tipo_accidentes)
else:
    st.write('Goodbye')


st.markdown('## Predicción')

st.write("holaaaa")

st.markdown('## Agrupamiento')
st.markdown('En esta sección puede seleccionar algún barrio y ver las características que posee')
nombre_barrio = st.selectbox(
    'Seleccione el nombre de barrio',
    df2['barrio'])

print(df.columns)
#x = np.array(literal_eval(df['location']))
#print(type(x))
#for i in df['location']:
     #print(np.array(literal_eval(i)))
    #print(i)
st.write(df2)
df3 = df.iloc[:100]
print(type(df['ubicacion_x'][0]))
st.write( df2[df2['barrio'] == 'Fátima']['cluster'].values)

st.write(map(nombre_barrio))
st.markdown('### Características del barrio ' + nombre_barrio)
st.markdown('Este barrio pertenece al grupo' )