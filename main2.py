import streamlit as st
import plotly.express as px
import pandas as pd

df = pd.read_csv('WHO_time_series.csv')

st.set_page_config(
    page_title="DashCovid",
    layout="wide")
st.title("DASHCOVID: Um Dashboard sobre os Dados de COVID-19 - 2020")
fig1 = px.line(df, x = 'Date_reported', y = 'Cumulative_cases')
fig1.show()
st.plotly_chart(fig1, use_container_width=True);
