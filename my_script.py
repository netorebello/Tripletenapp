import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles.csv') # lendo os dados
fig = px.histogram(car_data, x="odometer") # criar um histograma
fig.show()