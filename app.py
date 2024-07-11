import pandas as pd
import plotly.express as px
import streamlit as st
     
car_data = pd.read_csv('vehicles.csv') # lendo os dados
st.header('Histograma para Preço de venda de carros') #cabeçalho

hist_button = st.button('Criar histograma') # criar um botão
     
if hist_button: # se o botão for clicado
# escrever uma mensagem
    st.write('Criando um histograma para o preço de venda dos carros anunciados')
         
# criar um histograma
fig = px.histogram(car_data, x="price")
     
# exibir um gráfico Plotly interativo
st.plotly_chart(fig, use_container_width=True)

disp_button = st.button('Criar gráfico de dispersão')

if disp_button:
    st.write('Criando um gráfico de dispersão para o preço de venda dos carros anunciados')

    fig = px.scatter(car_data, x="price")

    st.plotly_chart(fig, use_container_width=True)
