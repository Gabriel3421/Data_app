import colunas
import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

st.write("Flores de iris")
st.sidebar.header("Input Params")

tracado = st.sidebar.selectbox(
    'Tracado_via',
    (
        'Reta',
        'Curva',
        'Cruzamento',
        'Intersecao de vias',
        'Desvio Temporario',
        'Viaduto',
        'Rotatoria',
        'Ponte',
        'Retorno Regulamentado',
        'Tunel'
     )
)

solo = st.sidebar.selectbox(
    'Uso_solo',
    (
        'Rural',
        'Urbano',
    )
)
quant_pessoas = st.sidebar.number_input(
    'Pessoas',
    0,
    100,
    0
)
quant_mortos = st.sidebar.number_input(
    'Mortos',
    0,
    100,
    0
)
quant_veiculos = st.sidebar.number_input(
    'Veiculos',
    0,
    100,
    0
)

tipos_veiculos = st.sidebar.multiselect(
    'Tipos de veiculos',
    (
        'Automovel',
        'Bicicleta',
        'Carrinho de mao',
        'Carroça/charrete',
        'Chassi/Plataforma',
        'Ciclomotor/Triciclo/Quadriciclo/Motoneta',
        'Microonibus',
        'Motocicletas',
        'MotorHome',
        'Reboque',
        'Semi/Reboque',
        'Side/car',
        'Trem/bonde',
        'Utilitario',
        'veiculo de medio/grande',
        'Onibus',
        'Outros'
     )
)
if (len(tipos_veiculos) > quant_veiculos):
    st.sidebar.warning('Selecione a mesma quantidade dos veiculos envolvidos, caso selecione um numero maior somente os '+ str(quant_veiculos) +' primeiros seram contabilizados.')

sepal_lenght = st.sidebar.slider('Sepal Lenght',4.3,7.9,5.4)
sepal_width = st.sidebar.slider('sepal width',2.0,4.4,3.4)
petal_lenght = st.sidebar.slider('petal Lenght',1.0,6.9,1.3)
petal_width = st.sidebar.slider('petal width',0.1,2.5,0.2)
data = {
    'sepal_lenght' : sepal_lenght,
    'sepal_width' : sepal_width,
    'petal_lenght' : petal_lenght,
    'petal_width' : petal_width
}
features = pd.DataFrame(data,index=[0])

st.subheader('User input params')
st.write(features)

iris = datasets.load_iris()
X = iris.data
Y = iris.target
clf = RandomForestClassifier()
clf.fit(X,Y)

prediction = clf.predict(features)
prediction_proba = clf.predict_proba(features)

st.subheader("Class labels and their corresponding index number")
st.write(iris.target_names)

st.subheader("pedriction")
st.write(iris.target_names[prediction])

st.subheader("pedriction probability")
st.write(prediction_proba)