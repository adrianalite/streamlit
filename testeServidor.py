#criando uma aplicação simples
import streamlit as st
#import no requirements.txt
import pandas as pd

df = pd.DataFrame({
    'nomeServidor': ['Adriana', 'Monica', 'Samara'],
    'salario': [1200,300,5000]
})
st.write("Criando uma tabela!")
#tabelas interativas
st.write(df)
#inserindo um selectbox
opcao = st.selectbox(
    'Qual servidor você gostaria de selecionar?',
     df['nomeServidor'])
#O formato de print é diferente de outras versões
#de Python
st.write('Você selecionou: ', opcao)
#como filtrar os dados pelo nome?
dadosFiltrados = df[df['nomeServidor'] == opcao]
st.write(dadosFiltrados)
