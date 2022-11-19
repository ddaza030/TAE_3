import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
from tabs import *
import pydeck as pdk
import operator
# from matplotlib import pyplot as plt
# from sklearn import preprocessing
# from sklearn.cluster import AgglomerativeClustering
# import scipy.cluster.hierarchy as sch
# from sklearn.cluster import KMeans
#pip install pydeck==0.7.1
image = Image.open('eeuu.png')
image1 = Image.open('university.png')
image2 = Image.open('bachelor.png')
image3 = Image.open('desarrollo2.png')

st.set_page_config(layout="wide", page_title="Aplicación web de clusters", page_icon=":taxi:")

#st.title('Aplicación web de clusters')


st.title('Aplicación web de segmentos de universidades en EEUU')

col1, col2, col3,col4 = st.columns(4)
with col1:
    st.image(image,width=80)
with col2:
    st.image(image2,width=80)
with col3:
    st.image(image1,width=80,use_column_width=100)



st.markdown('## Propósito')
st.markdown('El departamento de los Estados Unidos comparte información al público sobre las universidades del país, para que se puedan tomar decisiones respecto a la elección de universidades. El propósio de esta aplicación web es ayudar a futuros estudiantes de universidades en las áreas de Ciencias de la computación, Ingenierías, Ingenierías y tecnología y Matemáticas a escoger una universidad partiendo de segmentos de estas. ')

st.markdown('Para la selección de la universidad, se debe basar en los siguiente criterios:')
st.markdown('- **Tipo de universidad**: Ya sea pública, privada sin ánimo de lucro o privada con ánimo de lucro.')
st.markdown('- **Tipo de carrera:** Computación, ingeniería, ingeniería y tecnología o matemáticas.')
st.markdown('- **Modalidad de estudio:** Presencial o virtual.')
st.markdown('- **Porcentaje de estudiantes que reciben becas y prestamos:** Beca Pell Grants o préstamo federal.')
st.markdown('Con base a los criterios se dividieron las universidades en 6 segmentos. En esta aplicación web se podrá ver las características de cada uno de los segmentos. Además se podran comparar características de los segmentos.')

st.markdown('### Información adicional')
st.markdown('Se proporciona la siguiente información para que el aspirante pueda ahondar más y tomar una mejor decisión.')
st.markdown('Beca Pell Grants: https://www.youtube.com/watch?v=1pjYN4eSP1I&ab_channel=TheCollegeInvestor')
st.markdown('Prestamos federales: (FLoans) https://www.youtube.com/watch?v=1pjYN4eSP1I&ab_channel=TheCollegeInvestor')
st.markdown('Video sobre ingeniería: https://www.youtube.com/watch?v=I11y_FLlEp8&ab_channel=Explorist')
st.markdown('Video sobre ciencias de la computación: https://www.youtube.com/watch?v=I11y_FLlEp8&ab_channel=Explorist')
st.markdown('Reporte técnico base de la página: https://marloneau.quarto.pub/segmentacion-de-universidades-en-eeuu-con-enfasis-en-estudiantes-de-areas-relacionadas-a-la-computacion/#an%C3%A1lisis-de-resultados')
st.markdown('## Segmentos')




df = pd.read_csv('base1 (2).csv') 
df.rename({'Clusters': 'cluster'}, axis=1, inplace=True)


coordenadas = pd.read_csv('sinNulosyConCoordenadasEstado.csv')
coordenadas['Cluster'] = df['cluster'] 
coordenadas = coordenadas[["LONGITUDE", "LATITUDE","INSTNM",'Cluster', 'State']].dropna(axis = 0,subset = ["LONGITUDE", "LATITUDE"])




def map(numeroCluster, Estado):
    coordenadas_mask = coordenadas['Cluster'] == option
    estado_mask = coordenadas['State'] == option2

    coordenadas_show = coordenadas[coordenadas_mask & estado_mask]
    col1, col2, col3,col4, = st.columns(4)
    if(numeroCluster == 0):
        color = [255, 0, 0]
        cheap = Image.open('cheap.png')
        loans = Image.open('noloans.webp')
        bachelordegree = Image.open('bachelordegree.png')
        arrowD = Image.open('arrowD.png')
        st.markdown(f'### Universidades del Segmento 0 en {Estado}')
        with col1:
            st.image(cheap,width=100)
            st.markdown('- Universidades públicas')
        with col2:
            st.image(loans,width=100)
            st.markdown('- Menos cantidad de estudiantes con préstamos federales')
        with col3:
            st.image(bachelordegree,width=100)
            st.markdown('- Menos áreas de interés ofertadas')
        with col4:
            st.image(arrowD,width=100)
            st.markdown('- Menor porcentaje de estudiantes graduados en las áreas de interés estas universidades')
      
        
    elif(numeroCluster == 1):
        st.markdown(f'### Universidades del Segmento 1 en {Estado}')
        expensive = Image.open('expensive.png')
        prestamos = Image.open('prestamos.png')
        bachelordegree = Image.open('bachelordegree.png')
        arrowUp = Image.open('arrowU.png')
        with col1:
            st.image(expensive,width=100)
            st.markdown('- Mayoría de universidades con ánimos de lucro')
        with col2:
            st.image(prestamos,width=100)
            st.markdown(' - Más cantidad de estudiantes con préstamos federales y becas Pell Grants')
        with col3:
            st.image(bachelordegree,width=100)
            st.markdown('- Más oferta de carreras en modalidad presencial')
        with col4:
            st.image(arrowUp,width=100)
            st.markdown('- Mayor porcentaje de estudiantes graduados de estas universidades en las áreas de interés')
        color = [0, 255, 0]
    elif(numeroCluster == 2):
        st.markdown(f'### Universidades del Segmento 2 en {Estado}')
        expensive = Image.open('expensive.png')
        prestamos = Image.open('prestamos.png')
        bachelordegree = Image.open('bachelordegree.png')
        arrowUp = Image.open('arrowU.png')
        with col1:
            st.image(expensive,width=100)
            st.markdown('- Solo universidades privadas con ánimo de lucro')
        with col2:
            st.image(prestamos,width=100)
            st.markdown(' - Segundo con mayor cantidad de estudiantes con beca Pell Grants')
        with col3:
            st.image(bachelordegree,width=100)
            st.markdown('- Pocas áreas de interés ofertadas')
        with col4:
            st.image(arrowUp,width=100)
            st.markdown('- Segundo mayor en porcentaje de estudiantes graduados de estas universidades en computación e ingeniería y tecnología')
        color = [0, 0, 255]
    elif(numeroCluster == 3):
        st.markdown('### Universidades del Segmento 3')
        expensive = Image.open('expensive.png')
        prestamos = Image.open('prestamos.png')
        bachelordegree = Image.open('bachelordegree.png')
        arrowD = Image.open('arrowD.png')
        with col1:
            st.image(expensive,width=100)
            st.markdown('- Universidades públicas y privadas sin ánimos de lucro')
        with col2:
            st.image(prestamos,width=100)
            st.markdown(' - Segunda mayor deuda de estudiantes')
        with col3:
            st.image(bachelordegree,width=100)
            st.markdown('- Carreras únicamente de forma virtual')
        with col4:
            st.image(arrowD,width=100)
            st.markdown('- Bajo porcentaje de estudiantes graduados de estas universidades')
        color = [255, 255, 0]
    elif(numeroCluster == 4):
        st.markdown('### Universidades del Segmento 4')
        expensive = Image.open('universidad.png')
        prestamos = Image.open('prestamos.png')
        bachelordegree = Image.open('bachelordegree.png')
        arrowD = Image.open('arrowD.png')
        with col1:
            st.image(expensive,width=100)
            st.markdown('- Universidades públicas y privadas sin ánimos de lucro')
        with col2:
            st.image(prestamos,width=100)
            st.markdown(' - Mayor deuda media y menor cantidad de estudiantes con beca Pell Grants')
        with col3:
            st.image(bachelordegree,width=100)
            st.markdown('- Carreras únicamente ofertadas en modalidad presencial')
        with col4:
            st.image(arrowD,width=100)
            st.markdown('- Pocos estudiantes graduados en las áreas de interés, como en el segmento 3.')
        color = [255, 0, 255]
    elif(numeroCluster == 5):
        st.markdown('### Universidades del Segmento 5')
        expensive = Image.open('university.png')
        prestamos = Image.open('prestamos.png')
        bachelordegree = Image.open('bachelordegree.png')
        arrowUp = Image.open('arrowU.png')
        with col1:
            st.image(expensive,width=100)
            st.markdown('- Solo universidades privadas con ánimo de lucro.')
        with col2:
            st.image(prestamos,width=100)
            st.markdown(' - Tercer segmento con mayor cantidad de estudiantes con beca Pell Grants')
        with col3:
            st.image(bachelordegree,width=100)
            st.markdown('- Pocas áreas de interés ofertadas')
        with col4:
            st.image(arrowUp,width=100)
            st.markdown('- Mayor porcentaje de estudiantes graduados de estas universidades en ingeniería')
        color = [0, 255, 255]                  
    
    layer = pdk.Layer(
    "ScatterplotLayer",
    coordenadas_show,
    pickable=True,
    opacity=0.8,
    stroked=True,
    filled=True,
    radius_scale=50,
    radius_min_pixels=5,
    radius_max_pixels=100,
    line_width_min_pixels=1,
    get_position=["LONGITUDE", "LATITUDE"],
    get_radius="exits_radius",
    get_fill_color=color,
    get_line_color=[0, 0, 0],
)

# Set the viewport location
    view_state = pdk.ViewState(
        latitude=37.7749295, longitude=-122.4194155, zoom=6, min_zoom=0, max_zoom=15, bearing=0, pitch=0)

    # Render
    r = pdk.Deck(layers=[layer], initial_view_state=view_state,tooltip={"text": "{Nombre de la Universidad}"})
    return r



with st.sidebar:
    
    st.image(image3,width=80)
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


st.markdown('### Proporción de universidades por segmentos')


col4,col5 = st.columns(2)
    
with col4:
    st.markdown("Del gráfico de torda de la derecha podemos ver que:")
    st.markdown("- El 41% de las universidades están contenidas en el segmento 3.")
    st.markdown("- El 20% están contenidas en el segmento 1.")
    st.markdown("- El 17% están en el segmento 6.")
    st.markdown("- Los segmentos 2, 4 y 5 contienen menos del 10% de las universidades.")
#    st.markdown('#### Información sobre los segmentos')
#    st.markdown('')
#    st.markdown('##### Segmento 0')
#    st.markdown('Compuesto por universidades públicas, en donde está el menor porcentaje de estudiantes con un préstamo federal y por tanto la menor deuda media. Sin embargo es el segmento que contiene las universidades con menor oferta de las carreras de interés, por ende es donde menor cantidad de estudiantes graduados en dichos pregrados hay.')
#    st.markdown('##### Segmento 1')
#    st.markdown(' Compuesto por universidades en su mayoría privadas con ánimo de lucros y poseen un mayor porcentaje de estudiantes tanto con préstamo federal como con beca Pell Grants, debido a esto sus estudiantes tienen una deuda media mayor que los segmentos 0 y 2 y es el de mayor deuda media de sus estudiantes graduados (junto con los segmentos 3 y 4). En este segmento es donde se encuentran las universidades con mas oferta presencial de los campos de computación e ingeniería y tecnología, además es donde mayor porcentaje de estudiantes graduados en computación, ingeniería y tecnología y matemáticas hay.')
with col5:
    data = coordenadas['Cluster'].value_counts()
    st.pyplot(grafico_torta(data))
        
        

#col6,col7,col8,col9 = st.columns(4)
    
#with col6:
#    st.markdown('##### Segmento 2')
#    st.markdown('Compuesto únicamente por universidades privadas con ánimo de lucro similar al segmento 0 contiene las universidas con menor oferta de las carreras y menor deuda media de sus estudiantes, pero tiene una mayor oferta que el segmento 0 de computación en la modalidad virtual. Tiene un porcentaje de estudiantes con préstamo federal muy similar a los segmentos 3, 4 y 5 y es el segundo en cuanto a estudiantes con beca Pell Grants. Respecto a los graduados, es el de menor porcentaje de estos en las carreras salvo en computación y en ingeniería y tecnología que es el segundo mayor.')

#with col7:
#    st.markdown('##### Segmento 3')
#    st.markdown('Compuesto en su mayoría por universidades públicas y privadas sin ánimo de lucro las cuales no ofertan las carreras de forma presencial, únicamente virtual. A pesar de que tiene un porcentaje similar a los segmentos 2, 4 y 5 de estudiantes con préstamos federales, es el segmento con universidades cuyos estudiantes tienen la segunda mayor deuda media esto quizá provocado porque también tiene el segundo menor porcentaje de estudiantes con beca Pell Grants. Sus universidades son las de menor porcentaje de graduados (junto con el segmento 4) salvo en mátemáticas que tiene el segundo mayor porcentaje de graduados en este campo.')

#with col8:
#    st.markdown('##### Segmento 4')
#    st.markdown('Compuesto únicamente por universidades públicas y privadas sin ánimo de lucro (siendo mayor la cantidad de éstas ultimas en el segmento) las cuales ofertan las carreras únicamente de forma presencial. Como en el segmento 3 tiene un porcentaje similar de estudiantes con préstamos federales a los segmentos 2 y 5, pero es el segmento con universidades cuyos estudiantes tienen la mayor deuda media, ocasionado probablemente también porque es el de menor porcentaje de estudiantes con beca Pell Grants. Respecto al porcentaje de universidades graduados en sus universidades, ocurre aproximadamente lo mismo que en el segmento 3.')
#with col9:
#    st.markdown('##### Segmento 5')
#    st.markdown('Compuesto únicamente por universidades privadas sin ánimo de lucro, las universidades dentro de este grupo son similares en cuanto a su no oferta de las carreras como los segmentos 0 y 2, sin embargo tienen un poco más de oferta en los campos de computación y matemáticas en las modalidades presencial y virtual que estos 2 segmentos anteriormente mencionados. Su deuda media y porcentaje de estudiantes con préstamo federal son similares a los de segmento 1 y 4 respectivamente y es el tercero en cuanto a mayor media de porcentaje de estudiantes con becas Pell Grants. Destaca en que es el segmento con mayor porcentaje de graduados en ingeniería y en general es el tercero con mayor porcentaje de estudiantes graduados para las demás carreras.')

   
    #st.set_option('deprecation.showPyplotGlobalUse', False)
    
#st.markdown('### Mapa de las universidades')
#st.markdown('En el siguiente mapa se puede escoger las universidadades por segmento (cada universidad está representada con un circulo). Si pone el cursor encima del circulo, saldrá el nombre de la unviersidad.Para todos los segmentos o agrupaciones o segmentos, la mayoría de las universidades quedan al este de Estados Unidos.')
#st.markdown('##### Selección de variables')
#st.markdown('**Definición de las variables usadas para el análisis:**')
#st.markdown('**DEBT_MDN:** Se trata de la deuda mediana de préstamos acumulada en la institución por todos los estudiantes prestatarios de préstamos federales que se separan (es decir, se gradúan o se retiran) en un año fiscal determinado.')
#st.markdown('**PCTFLOAN:** proporción de estudiantes universitarios que recibieron préstamos federales en un año determinado.')
#st.markdown('**GRAD_DEBT_MDN:** deuda para los estudiantes que completarón sus estudios universitarios.')
#st.markdown('**PCTPELL:** esta variable es el porcentaje de estudiantes los cuales recibieron Pell Grants, el cual es una beca federal que reciben los estudiantes de ingresos bajos')
#st.markdown('**PCIP11:**: Porcentaje de titulos otorgados en el campo de la Computación')
#st.markdown('**PCIP14:** Porcentaje de titulos otorgados en el campo de la  ingeniería')
#st.markdown('**PCIP15:** Porcentaje de titulos otorgados en el campo de la  ingeniería y tecnología')
#st.markdown('**PCIP27:** Porcentaje de titulos en otorgados en el campo de la  matemáticas')
st.markdown('**A cada una de los siguientes campos asigneles un puntaje de 1 a 10 cuya suma final sea menor o igual 80**')


with st.form("my_form"):
    st.markdown("**Calificación de variables**")
    
    option_cat = st.selectbox(
    '¿Qué tipo de universidad prefiere?',
    ('Pública','Privada'))

    option_mod = st.selectbox(
    '¿Qué tipo de modalidad prefiere?',
    ('Presencial','Virtual'))

    option_1 = st.selectbox(
    '¿Qué importancia tiene para usted que la universidad tenga baja deuda media por parte de los estudiantes?',
    (0,1,2,3,4,5,6,7,8,9,10))

    option_2 = st.selectbox(
    '¿Qué importancia tiene para usted que la universidad tenga gran cantidad de estudiantes con préstamo federal?',
    (0,1,2,3,4,5,6,7,8,9,10))

    option_3 = st.selectbox(
    '¿Qué importancia tiene para usted que la universidad tenga baja deuda media por parte de los estudiantes graduados?',
    (0,1,2,3,4,5,6,7,8,9,10))

    option_4 = st.selectbox(
    '¿Qué importancia tiene para usted que la universidad tenga gran cantidad de estudiantes con beca Pell Grants?',
    (0,1,2,3,4,5,6,7,8,9,10))

    option_5 = st.selectbox(
    '¿Qué importancia tiene para usted que la universidad tenga gran porcentaje de titulos otorgados en el campo de la Computación?',
    (0,1,2,3,4,5,6,7,8,9,10))

    option_6 = st.selectbox(
    '¿Qué importancia tiene para usted que la universidad tenga gran porcentaje de titulos otorgados en el campo de la ingeniería?',
    (0,1,2,3,4,5,6,7,8,9,10))

    option_7 = st.selectbox(
    '¿Qué importancia tiene para usted que la universidad tenga gran porcentaje de titulos otorgados en el campo de la ingeniería y tecnología?',
    (0,1,2,3,4,5,6,7,8,9,10))

    option_8 = st.selectbox(
    '¿Qué importancia tiene para usted que la universidad tenga gran porcentaje de titulos otorgados en el campo de las matemáticas?',
    (0,1,2,3,4,5,6,7,8,9,10))

# Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
            if(option_1 + option_2 + option_3 + option_4 + option_5 + option_6+ option_7 + option_8 <= 80):
                diccionario =  dict([('DEBT_MDN',option_1) , ('PCTFLOAN',option_2) , ('GRAD_DEBT_MDN',option_3) ,('PCTPELL',option_4) , ('PCIP11',option_5),('PCIP14',option_6),('PCIP15',option_7),('PCIP27',option_8)])
                diccionario_sorted = sorted(diccionario.items(), key=operator.itemgetter(1), reverse=True)
                st.write('### Segmentos recomendados')
                if(option_cat == 'Pública'):
                    if(diccionario_sorted[0][0] == 'DEBT_MDN'):
                        st.write('### Segmento 0')
                    if((diccionario_sorted[0][0] == 'PCTFLOAN') or (diccionario_sorted[0][0] == 'PCTPELL') or (option_mod == "Presencial") or (diccionario_sorted[0][0] == 'PCIP11') or  (diccionario_sorted[0][0] == 'PCIP14') or (diccionario_sorted[0][0] == 'PCIP15') or  (diccionario_sorted[0][0] == 'PCIP27')):
                        st.write('### Segmento 1')
                    
                    if((option_mod == 'Virtual') or (diccionario_sorted[0][0] == 'PCIP27')):
                        st.write('### Segmento 3')
                    
                    if((option_mod == 'Presencial')):
                        st.write('### Segmento 4')

                if((option_cat == 'Privada')):

                    if((diccionario_sorted[0][0] == 'PCTFLOAN') or (diccionario_sorted[0][0] == 'PCTPELL') or (option_mod == "Presencial") or (diccionario_sorted[0][0] == 'PCIP11') or  (diccionario_sorted[0][0] == 'PCIP14') or (diccionario_sorted[0][0] == 'PCIP15') or  (diccionario_sorted[0][0] == 'PCIP27')):
                        st.write('### Segmento 1')

                    if((diccionario_sorted[0][0] == 'PCTPELL') or (diccionario_sorted[0][0] == 'PCTPELL') or (diccionario_sorted[0][0] == 'PCIP14') or (diccionario_sorted[0][0] == 'PCIP11')):
                        st.write('### Segmento 2')

                    if((option_mod == 'Virtual') or (diccionario_sorted[0][0] == 'PCIP27')):
                        st.write('### Segmento 3')

                    if((option_mod == 'Presencial')):
                        st.write('### Segmento 4')

                    if((diccionario_sorted[0][0] == 'DEBT_MDN') or (diccionario_sorted[0][0] == 'PCIP15') ):
                        st.write('### Segmento 5')

                        

            else:
                st.write("Revisar la distribución de los puntos, la suma de estos debe ser igual a 10.")



st.markdown('##### Seleccione el segmento')
option = st.selectbox(
    'Seleccione el (o uno de los) segmentos recomendados para visualizarlo:',
    (0,1,2,3,4,5))
x = option
segmento = x

option2 = st.selectbox(
    'seleccione el estado',
    list(coordenadas['State'].unique()))
y = option2
estado = y

st.write("Teniendo en cuenta el segmento de universidades recomendado, a continuación se presentan los nombres de las universidades del  segmento y su respectiva ubicación en el mapa")
coordenadas = coordenadas.rename(columns = {"INSTNM":"Nombre de la Universidad"})
st.dataframe(coordenadas[coordenadas['Cluster'] == option]['Nombre de la Universidad'].reset_index(drop=True))

st.write(map(segmento, estado))








    