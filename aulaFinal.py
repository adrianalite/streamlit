#Gráficos treemap usando streamlit
import streamlit as st

st.bar_chart(dfMulheres['siglaPartido'].value_counts())
