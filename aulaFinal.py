'''import requests as rq
import pandas as pd
import streamlit as st

#carregando o dataframe de mulheres
url = 'https://dadosabertos.camara.leg.br/api/v2/deputados?siglaSexo=F&ordem=ASC&ordenarPor=nome'
resposta = rq.get(url)
dadosJSON = resposta.json()
dfMulheres = pd.DataFrame(dadosJSON['dados'])

#carregando o dataframe de mulheres
url = 'https://dadosabertos.camara.leg.br/api/v2/deputados?siglaSexo=M&ordem=ASC&ordenarPor=nome'
resposta = rq.get(url)
dadosJSON = resposta.json()
dfHomens = pd.DataFrame(dadosJSON['dados'])

st.bar_chart(dfMulheres['siglaPartido'].value_counts())'''

import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.bar_chart(chart_data)




