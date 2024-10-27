

"""#Estudo de caso

- Apresentar a página e base de dados usada
https://www.ibge.gov.br/geociencias/organizacao-do-territorio/estrutura-territorial/27385-localidades.html?edicao=40668&t=downloads
- Informar como subir para o git um arquivo csv
- Informar que a fase agora é de limpeza dos dados
e criação de grafico de dispersão com mapas
- A dinâmica deste estudo de caso é diferente. Vou mostrar a jornada do herói (erros e acertos na elaboração do codigo. Comparar com um texto).
"""

#instalando o streamlit
!pip install streamlit

import streamlit as st
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/adrianalite/datasets/main/BR_LQs_CD2022.csv')
df.head()

#excluindo a coluna Unnamed
df.drop(columns=['Unnamed: 0'], inplace=True)
df.head()

#programa anterior (questão assíncrona)
import streamlit as st
import pandas as pd

st.title('Localização das comunidades quilombolas (2022)')
df = pd.read_csv('https://raw.githubusercontent.com/adrianalite/datasets/main/BR_LQs_CD2022.csv')

#quantidade de comunidades por estado
df['NM_UF'].value_counts()

#sugestões de incrementos para a questão 6
import streamlit as st;
import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/adrianalite/datasets/main/BR_LQs_CD2022.csv')

#dados sobre estatística descritiva
qtdeMunicipios = len(df['NM_MUNIC'].unique())
st.write("A quantidade de municípios com localização quilombola é " + str(qtdeMunicipios))

qtdeComunidades = len(df['NM_AGLOM'].unique())
st.write("A quantidade de comunidades quilombolas é " + str(qtdeComunidades))

df.info()
#é necessário o tratamento dos dados para
#latitude e longitude

#vendo as colunas
df.columns

#convertendo para números
list = ['Lat_d', 'Long_d']
df[list] = df[list].apply(pd.to_numeric, errors='coerce')
df.info()

#fazendo o tratamento dos dados
#fillna
df.fillna(0, inplace=True)
df.drop(columns=['Unnamed: 0'], inplace=True)

#inserindo um selectbox
estadoFiltro = st.selectbox(
    'Qual estado selecionar?',
     df['NM_UF'])

dadosFiltrados = df[df['NM_UF'] == estadoFiltro]

#Erro: Tem mais de um estado na lista!
estadoFiltro = st.selectbox(
    'Qual estado selecionar?',
     df['NM_UF'].unique())

dadosFiltrados = df[df['NM_UF'] == estadoFiltro]

#inserindo o título
import streamlit as st
import pandas as pd

st.title('Localização das comunidades quilombolas (2022)')

#Mostrar tabela
if st.checkbox('Mostrar tabela'):
  st.write(df)

#gráficos das questões anteriores

#número de comunidades por estado
st.header('Número de comunidades por UF')
st.bar_chart(df['NM_UF'].value_counts())

#os dez municípios com mais comunidades
st.header('Os dez municípios com mais comunidades quilombolas')
st.bar_chart(df['NM_MUNIC'].value_counts()[:10])

#dados sobre estatística descritiva
qtdeMunicipios = len(df['NM_MUNIC'].unique())
#st.write("A quantidade de municípios com localização quilombola é " + str(qtdeMunicipios))
st.metric('# Municípios', qtdeMunicipios)

qtdeComunidades = len(df['NM_AGLOM'].unique())
#st.write("A quantidade de comunidades quilombolas é " + str(qtdeComunidades))
st.metric('# Comunidades', qtdeComunidades)

#documentação do streamlit para metric
#https://docs.streamlit.io/develop/api-reference/data/st.metric

#criando duas colunas para os dados
colunas = st.columns(2)
colunas[0].metric('# Municípios', len(df['NM_MUNIC'].unique()))
colunas[1].metric('# Comunidades', len(df['NM_AGLOM'].unique()))

#versao completa com colunas
import streamlit as st
import pandas as pd

st.title('Localização das comunidades quilombolas (2022)')
df = pd.read_csv('https://raw.githubusercontent.com/adrianalite/datasets/main/BR_LQs_CD2022.csv')

#limpando os dados
df.fillna(0, inplace=True)
df.drop(columns=['Unnamed: 0'], inplace=True)
list = ['Lat_d', 'Long_d']
#convertendo para numeros
df[list] = df[list].apply(pd.to_numeric, errors='coerce')

estados = df['NM_UF'].unique()
estadoFiltro = st.selectbox(
    'Qual estado selecionar?',
     estados)
dadosFiltrados = df[df['NM_UF'] == estadoFiltro]
if st.checkbox('Mostrar tabela'):
  st.write(dadosFiltrados)

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

#Conclusões
#A limpeza dos dados é o processo onde mais passamos tempo
#O processo de construção do dashboard é interativo e incremental.
#Devemos sempre usar a documentação para aprendar como melhorar o código.
