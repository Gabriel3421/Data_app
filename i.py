# -*- coding: utf-8 -*-
from colunas import *
from joblib import load
import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

clf = load('Mlp_classificador.joblib')

st.sidebar.header("Input Params")
causa = st.sidebar.selectbox(
    'Causa do Acidente',
    ('Outras',
     'Animais na Pista',
      'Não guardar distância de segurança',
      'Falta de atenção',
      'Velocidade Incompatível',
      'Desobediência à sinalização',
      'Defeito Mecânico no Veículo',
      'Ingestão de Álcool',
      'Dormindo',
      'Ultrapassagem Indevida',
      'Defeito na Via',
      'Falta de Atenção à Condução',
      'Desobediência às normas de trânsito pelo condutor',
      'Condutor Dormindo',
      'Falta de Atenção do Pedestre',
      'Pista Escorregadia',
      'Avarias e/ou desgaste excessivo no pneu',
      'Sinalização da via insuficiente ou inadequada',
      'Mal Súbito',
      'Carga excessiva e/ou mal acondicionada',
      'Restrição de Visibilidade',
      'Objeto estático sobre o leito carroçável',
      'Deficiência ou não Acionamento do Sistema de Iluminação/Sinalização do Veículo',
      'Fenômenos da Natureza',
      'Ingestão de Substâncias Psicoativas',
      'Agressão Externa',
      'Desobediência às normas de trânsito pelo pedestre',
      'Ingestão de álcool e/ou substâncias psicoativas pelo pedestre')
)
tipoacidente = st.sidebar.selectbox(
    'Tipo Acidente',
    ('Atropelamento de Animal',
       'Atropelamento de Pedestre',
       'Atropelamento de animal',
       'Atropelamento de pessoa',
       'Capotamento',
       'Colisão Transversal',
       'Colisão com bicicleta',
       'Colisão com objeto em movimento',
       'Colisão com objeto estático',
       'Colisão com objeto fixo',
       'Colisão com objeto móvel',
       'Colisão frontal',
       'Colisão lateral',
       'Colisão transversal',
       'Colisão traseira',
       'Danos Eventuais',
       'Danos eventuais',
       'Derramamento de Carga',
       'Derramamento de carga',
       'Engavetamento',
       'Incêndio',
       'Queda de motocicleta / bicicleta / veículo',
       'Queda de ocupante de veículo',
       'Saída de Pista',
       'Saída de leito carroçável',
       'Tombamento')
)

metereologica = st.sidebar.selectbox(
    'Condição Metereologica',
    ('Ceu Claro',
      'Chuva',
      'Nublado',
      'Sol',
      'Nevoeiro/neblina',
      'Ignorada',
      'Granizo',
      'Vento',
      'Neve',
      'Garoa/Chuvisco',
      'Céu Claro',
      'Nevoeiro/Neblina')
)


fasedia = st.sidebar.selectbox(
    'Fase do dia',
    ('Pleno dia',
      'Plena noite',
      'Anoitecer',
      'Amanhecer',
      'Plena Noite',
      'Valor não definido')
)


sentidovia = st.sidebar.selectbox(
    'Sentido da Via',
    ('Crescente',
    'Decrescente')
)

tipopista = st.sidebar.selectbox(
    'Tipo da Pista',
    ('Simples',
      'Dupla',
      'Múltipla')
)


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
        'Trator',
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

def tp_automoveis(tipos_veiculos):
    automovel, bicicleta, carrinhodemao, carroça = 0,0,0,0
    chassi, ciclomotor,microonibus,motocicletas = 0,0,0,0
    motorHome,reboque,semi_reboque,sidecar = 0,0,0,0
    trembonde, utilitario, veiculomediogrande,onibus,trator,outros = 0,0,0,0,0,0

    tpv = [automovel, bicicleta, carrinhodemao, carroça,
            chassi, ciclomotor,microonibus,motocicletas,
            motorHome,reboque,semi_reboque,sidecar,
            trembonde, utilitario, veiculomediogrande,onibus,trator,outros]

    tpv2 = ['Automovel',
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
            'Trator',
            'Outros']


    for i in range(len(tipos_veiculos)):
        for j in range(len(tpv2)):
            if(tipos_veiculos[i] == tpv2[j]):
                tpv[j] = 1;
                print(tipos_veiculos[i])

    return tpv

tpv = tp_automoveis(tipos_veiculos)
datas = {
    'causa_acidente': causa_acidente[causa],
    'tipo_acidente': tipo_acidente[tipoacidente],
    'fase_dia': fase_dia[fasedia],
    'sentido_via': sentido_via[sentidovia],
    'condicao_metereologica': condicao_metereologica[metereologica],
    'tipo_pista': tipo_pista[tipopista],
    'tracado_via': tracado_via[tracado],
    'uso_solo': uso_solo[solo],
    'pessoas': quant_pessoas,
    'mortos': quant_mortos,
    'veiculos': quant_veiculos,
    '0':0,
    'Automóvel': tpv[0],
    'Bicicleta':tpv[1],
    'Carro de mão':tpv[2],
    'Carro-de-mao':tpv[2],
    'Carroça-charrete':tpv[3],
    'Chassi-plataforma':tpv[4],
    'Ciclomotor-Triciclo-Quadriciclo-Motoneta':tpv[5],
    'Microônibus':tpv[6],
    'Motocicletas':tpv[7],
    'Motor-Casa':tpv[8],
    'Reboque':tpv[9],
    'Semi-Reboque':tpv[10],
    'Side-car':tpv[11],
    'Trem-bonde':tpv[12],
    'Utilitário':tpv[13],
    'veiculo de medio-grande':tpv[14],
    'Ônibus':tpv[15],
    'Trator':tpv[16],
    'Outros':tpv[17]
    
}

features = pd.DataFrame(datas,index=[0])
print(features)

st.header("Classificador")

prediction = clf.predict(features)
prediction_proba = clf.predict_proba(features)
print(prediction)
print(prediction_proba)
st.subheader("Predriction")
st.write(pd.DataFrame({'Conclusao': prediction}))
st.subheader("Predriction probability")
st.write(pd.DataFrame(
    {
        'Com Vítimas Fatais': prediction_proba[0][0],
        'Com Vítimas Feridas': prediction_proba[0][1],
        'Sem Vítimas': prediction_proba[0][2],
    }, index=[0]))
