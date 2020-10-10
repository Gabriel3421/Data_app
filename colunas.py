# -*- coding: utf-8 -*-
tracado_via = {
  'Reta': 0,
  'Curva': 1,
  'Cruzamento': 2,
  'Intersecao de vias': 3,
  'Desvio Temporario': 4,
  'Viaduto': 5,
  'Rotatoria': 6,
  'Ponte': 7,
  'Retorno Regulamentado': 8,
  'Tunel': 9
}

uso_solo = {
  'Rural': 0,
  'Urbano': 1,
}

causa_acidente = {
  'Outras':0,
  'Animais na Pista':1,
  'Não guardar distância de segurança':2,
  'Falta de atenção':3,
  'Velocidade Incompatível':4,
  'Desobediência à sinalização':5,
  'Defeito Mecânico no Veículo':6,
  'Ingestão de Álcool':7,
  'Dormindo':8,
  'Ultrapassagem Indevida':9,
  'Defeito na Via':10,
  'Falta de Atenção à Condução':11,
  'Desobediência às normas de trânsito pelo condutor':12,
  'Condutor Dormindo':13,
  'Falta de Atenção do Pedestre':14,
  'Pista Escorregadia':15,
  'Avarias e/ou desgaste excessivo no pneu':16,
  'Sinalização da via insuficiente ou inadequada':17,
  'Mal Súbito':18,
  'Carga excessiva e/ou mal acondicionada':19,
  'Restrição de Visibilidade':20,
  'Objeto estático sobre o leito carroçável':21,
  'Deficiência ou não Acionamento do Sistema de Iluminação/Sinalização do Veículo':22,
  'Fenômenos da Natureza':23,
  'Ingestão de Substâncias Psicoativas':24,
  'Agressão Externa':25,
  'Desobediência às normas de trânsito pelo pedestre':26,
  'Ingestão de álcool e/ou substâncias psicoativas pelo pedestre':27
}

tipo_pista = {
  'Simples':0,
  'Dupla':1,
  'Múltipla':2
}
tipo_acidente = {
   'Atropelamento de Animal': 18,
   'Atropelamento de Pedestre': 20,
   'Atropelamento de animal': 2,
   'Atropelamento de pessoa': 8,
   'Capotamento': 10,
   'Colisão Transversal': 5,
   'Colisão com bicicleta': 13,
   'Colisão com objeto em movimento': 22,
   'Colisão com objeto estático': 17,
   'Colisão com objeto fixo': 7,
   'Colisão com objeto móvel': 14,
   'Colisão frontal': 0,
   'Colisão lateral': 3,
   'Colisão transversal': 21,
   'Colisão traseira': 4,
   'Danos Eventuais': 9,
   'Danos eventuais': 24,
   'Derramamento de Carga': 12,
   'Derramamento de carga': 25,
   'Engavetamento': 23,
   'Incêndio': 15,
   'Queda de motocicleta / bicicleta / veículo': 11,
   'Queda de ocupante de veículo': 16,
   'Saída de Pista': 1,
   'Saída de leito carroçável': 19,
   'Tombamento': 6
}
condicao_metereologica = {
  'Ceu Claro':0,
  'Chuva':1,
  'Nublado':2,
  'Sol':3,
  'Nevoeiro/neblina':4,
  'Ignorada':5,
  'Granizo':7,
  'Vento':6,
  'Neve':8,
  'Garoa/Chuvisco':9,
  'Céu Claro':10,
  'Nevoeiro/Neblina':11
}
fase_dia = {
  'Pleno dia':0,
  'Plena noite':1,
  'Anoitecer':3,
  'Amanhecer':2,
}
sentido_via = {
  'Crescente':1,
  'Decrescente':0
  }