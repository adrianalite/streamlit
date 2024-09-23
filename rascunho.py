#sugestões de incrementos para a questão 6
import streamlit as st;
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/adrianalite/datasets/main/BR_LQs_CD2022.csv')
st.write(df)

#dados sobre estatística descritiva
qtdeMunicipios = df['NM_MUNIC'].unique()
st.write("A quantidade de municípios com localização quilombola é " + qtdeMunicipios)

qtdeComunidades = df['NM_AGLOM'].unique()
st.write("A quantidade de comunidades quilombolas é " + str(qtdeComunidades))

#os dez municípios com mais comunidades
st.header('Os dez municípios com mais comunidades quilombolas')
st.bar_chart(df['NM_MUNIC'].value_counts()[:10])
