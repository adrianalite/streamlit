import streamlit as st
number = st.slider("Selecione um número: ", min_value=1, max_value=10)
st.text("Seu número é " + str(number))
