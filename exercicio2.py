import streamlit as st
import pandas as pd

df = pd.DataFrame({
    'Nome do servidor': ['Adriana', 'Monica', 'Samara'],
    'Salario': [1200,300,5000]
})

st.write("Criando uma tabela!")

#tabelas interativas
st.write(df) 

#inserindo um selectbox
option = st.selectbox(
    'Qual servidor você gostaria de selecionar?',
     df['Nome do servidor'])

st.write('You selected: ', option)
