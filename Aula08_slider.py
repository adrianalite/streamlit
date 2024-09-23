import streamlit as st
import pandas as pd

st.title('Localização das comunidades quilombolas (2022)')

df = pd.read_csv('https://raw.githubusercontent.com/adrianalite/datasets/main/BR_LQs_CD2022.csv')
df.info()
numero = st.slider('Selecione um número de linhas a serem exibidas', min_value = 0, max_value = 100)
st.write(df.head(numero))
df['NM_UF'].value_counts()
st.bar_chart(df['NM_UF'].value_counts())
