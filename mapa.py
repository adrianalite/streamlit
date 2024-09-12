#inserindo o título
import streamlit as st
import pandas as pd

st.title('Localização das comunidades quilombolas (2022)')

df = pd.read_csv('https://raw.githubusercontent.com/adrianalite/datasets/main/BR_LQs_CD2022.csv', sep=';')
df.head()

#Mostrar tabela
if st.checkbox('Mostrar tabela'):
  st.table(dadosFiltrados)

#fillna
df.fillna(0, inplace=True)
list = ['Lat_d', 'Long_d']
df[list] = df[list].apply(pd.to_numeric, errors='coerce')
df.rename(columns={'Lat_d': 'LATITUDE', 'Long_d':'LONGITUDE'}, inplace=True)
estados = df['NM_UF'].unique()
estadoFiltro = st.selectbox(
    'Qual estado selecionar?',
     estados)

dadosFiltrados = df[df['NM_UF'] == estadoFiltro]
st.map(dadosFiltrados)
