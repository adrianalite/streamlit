#programa apresentado durante a aula
import streamlit as st
import pandas as pd

st.title('Localização das comunidades quilombolas (2022)')
df = pd.read_csv('https://raw.githubusercontent.com/adrianalite/datasets/main/BR_LQs_CD2022.csv')

#apresentar o dataframe
#https://www.ibge.gov.br/geociencias/organizacao-do-territorio/estrutura-territorial/27385-localidades.html?=&t=downloads

df.info()
numero = st.slider('Selecione um número de linhas a serem exibidas', min_value = 0, max_value = 100)
st.write(df.head(numero))

#quantidade de comunidades por estado
df['NM_UF'].value_counts()

#número de comunidades por estado
st.header('Número de comunidades por UF')
st.bar_chart(df['NM_UF'].value_counts())

#sugestões de incrementos para a questão 6
import streamlit as st;
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/adrianalite/datasets/main/BR_LQs_CD2022.csv')

#dados sobre estatística descritiva
qtdeMunicipios = len(df['NM_MUNIC'].unique())
#st.write("A quantidade de municípios com localização quilombola é " + str(qtdeMunicipios))
st.metric('Municípios', qtdeMunicipios)

qtdeComunidades = len(df['NM_AGLOM'].unique())
st.write("A quantidade de comunidades quilombolas é " + str(qtdeComunidades))

#os dez municípios com mais comunidades
st.header('Os dez municípios com mais comunidades quilombolas')
st.bar_chart(df['NM_MUNIC'].value_counts()[:10])
