import requests as rq
import pandas as pd
import streamlit as st

#identificando as mulheres

url = 'https://dadosabertos.camara.leg.br/api/v2/deputados?siglaSexo=F&ordem=ASC&ordenarPor=nome'
resposta = rq.get(url)
dadosJSON = resposta.json()
dfMulheres = pd.DataFrame(dadosJSON['dados'])
dfMulheres['sexo'] = 'F'

#identificando os homens
url = 'https://dadosabertos.camara.leg.br/api/v2/deputados?siglaSexo=M&ordem=ASC&ordenarPor=nome'
resposta = rq.get(url)
dadosJSON = resposta.json()
dfHomens = pd.DataFrame(dadosJSON['dados'])
dfHomens['sexo'] = 'M'

#unindo os dataframes
df = pd.concat([dfMulheres, dfHomens])

#ocorrencias totais
ocorrencias = df['siglaUf'].value_counts()
dfEstados = pd.DataFrame({
    'siglaUf': ocorrencias.index,
    'quantidade': ocorrencias.values}
    )

#ocorrências sobre as mulheres
ocorrenciasMulheres = dfMulheres['siglaUf'].value_counts()
dfEstadosMulheres = pd.DataFrame({
    'siglaUf': ocorrenciasMulheres.index,
    'quantidade': ocorrenciasMulheres.values}
    )

#ocorrências sobre os homens
ocorrenciasHomens = dfHomens['siglaUf'].value_counts()
dfEstadosHomens = pd.DataFrame({
    'siglaUf': ocorrenciasHomens.index,
    'quantidade': ocorrenciasHomens.values}
    )

st.title('Dados sobre os deputados')
st.dataframe(df)
st.write('Total de deputadas mulheres por estado')
st.bar_chart(dfEstadosMulheres, x = 'siglaUf', y = 'quantidade', x_label='Siglas dos estados', y_label='Quantidade de deputados')

st.write('Total de deputados homens por estado')
st.bar_chart(dfEstadosHomens, x = 'siglaUf', y = 'quantidade', x_label='Siglas dos estados', y_label='Quantidade de deputados')

st.write('Total de deputados estado')
st.bar_chart(dfEstados, x = 'siglaUf', y = 'quantidade', x_label='Siglas dos estados', y_label='Quantidade de deputados')
