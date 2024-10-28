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

#Filtrando df por sexo
#inserindo um selectbox
opcao = st.selectbox(
    'Qual o sexo?',
     df['sexo'].unique())

dfFiltrado = df[df['sexo'] == opcao]
st.title('Deputados do sexo ' + opcao)

#ocorrencias totais
ocorrencias = dfFiltrado['siglaUf'].value_counts()
dfEstados = pd.DataFrame({
    'siglaUf': ocorrencias.index,
    'quantidade': ocorrencias.values}
    )

#total de deputados
total = df['id'].count()
st.metric('Total de deputados', total)

#Porcentagem de homens
totalHomens = dfHomens['id'].count()
st.metric('Porcentagem de Homens', totalHomens/total * 100)

#total de mulheres
totalMulheres = dfMulheres['id'].count()
st.metric('Porcentagem de Mulheres', totalMulheres/total * 100)

st.write('Total de deputadas do sexo ' + opcao)
st.bar_chart(dfEstados, x = 'siglaUf', y = 'quantidade', x_label='Siglas dos estados', y_label='Quantidade de deputados')

st.dataframe(dfFiltrado)

url = 'https://dadosabertos.camara.leg.br/api/v2/deputados/204528/despesas?ordem=ASC&ordenarPor=ano'

resposta = rq.get(url)
dadosJSON = resposta.json()
df = pd.DataFrame(dadosJSON['dados'])
#calculando os gastos
gastos = df['valorLiquido'].sum()
nomeDeputado = df['nome'].iloc[0]

st.title('Gastos do deputado ' + nomeDeputado + nomeDeputado)
st.metric('Gastos do deputado', gastos)
