import pandas as pd
import plotly.express as px
import streamlit as st
     
data = pd.read_csv('vehicles.csv') # lendo os dados
st.header('App para análise de dados de carros anunciados') #cabeçalho

# Função para incluir fabricantes com menos de 1000 anúncios
def filter_manufacturers(data, threshold=1000):
    manufacturer_counts = data['model'].value_counts()
    filtered_manufacturers = manufacturer_counts[manufacturer_counts < threshold].index
    return data[data['model'].isin(filtered_manufacturers)]

# Visualizador de Dados
st.subheader('Visualizador de Dados')

if st.button('Incluir Fabricantes com Menos de 1000 Anúncios'):
    filtered_data = filter_manufacturers(data)
    st.write(filtered_data)
else:
    st.write(data)

# Tipos de Veículos por Fabricante
st.subheader('Tipos de Veículos por Fabricante')

vehicle_types_by_manufacturer = data.groupby(['model', 'type']).size().reset_index(name='counts')
fig_vehicle_types = px.bar(vehicle_types_by_manufacturer, x='model', y='counts', color='type', title='Tipos de Veículos por Fabricante')
st.plotly_chart(fig_vehicle_types)

# Histograma de Condição Vs Ano do Modelo
st.subheader('Histograma de Condição Vs Ano do Modelo')

fig_condition_model_year = px.histogram(data, x='model_year', color='condition', title='Condição Vs Ano do Modelo')
st.plotly_chart(fig_condition_model_year)

# Comparador de Preço entre Fabricantes
st.subheader('Comparador de Preço entre Fabricantes')

manufacturers = data['model'].unique()
manufacturer_1 = st.selectbox('Selecione o Primeiro Fabricante', manufacturers)
manufacturer_2 = st.selectbox('Selecione o Segundo Fabricante', manufacturers)

if manufacturer_1 and manufacturer_2:
    filtered_data_1 = data[data['model'] == manufacturer_1]
    filtered_data_2 = data[data['model'] == manufacturer_2]

    fig_price_comparison = px.scatter(filtered_data_1, x='odometer', y='price', color=px.Constant(manufacturer_1), labels={'color': 'Fabricante'}, title='Comparador de Preço entre Fabricantes')
    fig_price_comparison.add_scatter(x=filtered_data_2['odometer'], y=filtered_data_2['price'], mode='markers', name=manufacturer_2)

    st.plotly_chart(fig_price_comparison)