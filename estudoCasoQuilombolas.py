#versao completa com colunas
import streamlit as st
import pandas as pd

st.title('Localização das comunidades quilombolas (2022)')
df = pd.read_csv('https://raw.githubusercontent.com/adrianalite/datasets/main/BR_LQs_CD2022.csv')

#limpando os dados
df.fillna(0, inplace=True)
df.drop(columns=['Unnamed: 0'], inplace=True)
list = ['Lat_d', 'Long_d']
#testando
df = df.replace(to_replace=[None], value=0)
df.rename(columns={'Lat_d': 'LATITUDE', 'Long_d':'LONGITUDE'}, inplace=True)
estados = df['NM_UF'].unique()
estadoFiltro = st.selectbox(
    'Qual estado selecionar?',
     estados)
dadosFiltrados = df[df['NM_UF'] == estadoFiltro]
if st.checkbox('Mostrar tabela'):
  st.write(dadosFiltrados)
st.map(dadosFiltrados)

#dados sobre estatística descritiva
qtdeMunicipios = len(df['NM_MUNIC'].unique())
qtdeComunidades = len(df['NM_AGLOM'].unique())

#criando duas colunas para os dados
colunas = st.columns(2)
colunas[0].metric('# Municípios', len(df['NM_MUNIC'].unique()))
colunas[1].metric('# Comunidades', len(df['NM_AGLOM'].unique()))

#número de comunidades por estado
st.header('Número de comunidades por UF')
st.bar_chart(df['NM_UF'].value_counts())

#os dez municípios com mais comunidades
st.header('Os dez municípios com mais comunidades quilombolas')
st.bar_chart(df['NM_MUNIC'].value_counts()[:10])
