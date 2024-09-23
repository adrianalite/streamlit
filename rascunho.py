#acessando a api de dados
url = 'https://brasilapi.com.br/api/cvm/corretoras/v1'
import requests as rq
resposta = rq.get(url)
dadosJSON = resposta.json()

#criando o dataframe
import pandas as pd
df = pd.DataFrame(dadosJSON)
dfFiltrado = df.loc[:, ['nome_comercial', 'valor_patrimonio_liquido', 'data_patrimonio_liquido', 'municipio', 'uf']]

regioes = {
    'Norte': ['AC', 'AP', 'AM', 'PA', 'RO', 'RR', 'TO'],
    'Nordeste': ['AL', 'BA', 'CE', 'MA', 'PB', 'PE', 'PI', 'RN', 'SE'],
    'Centro-Oeste': ['DF', 'GO', 'MT', 'MS'],
    'Sudeste': ['ES', 'MG', 'RJ', 'SP'],
    'Sul': ['PR', 'RS', 'SC']
}

# Função para classificar o estado pela região
def classificar_regiao(estado):
    for regiao, estados in regioes.items():
        if estado in estados:
            return regiao
    return 'Estado não encontrado'

# Exemplo de uso
estados = dfFiltrado['uf']

# Aplicar a função de classificação aos estados

classificacoes = [classificar_regiao(estado) for estado in estados]
dfFiltrado['regiao'] = classificacoes

#retirando espaços dos campos
dfFiltrado = dfFiltrado[(dfFiltrado != '').all(axis=1)]

#criando o dashboard
import streamlit as st
import matplotlib.pyplot as plt

st.title('Corretoras do Brasil')

fig1, ax = plt.subplots()
plt.figure(figsize=(10, 6))
ax.pie(dfFiltrado['regiao'].value_counts(), labels=dfFiltrado['regiao'].value_counts().index, autopct='%1.1f%%')
ax.set_xlabel('Região')
ax.set_ylabel('Quantidade')
ax.set_title('Quantidade de corretoras por região')

st.pyplot(fig1)
