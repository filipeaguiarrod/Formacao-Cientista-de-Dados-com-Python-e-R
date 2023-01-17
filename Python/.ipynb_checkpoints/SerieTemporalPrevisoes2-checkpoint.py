import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from statsmodels.tsa.arima_model import ARIMA
from pmdarima.arima import auto_arima

base = pd.read_csv('AirPassengers.csv')
dateparse = lambda dates: pd.datetime.strptime(dates,'%Y-%m') # transformar objeto em data (ano-mes)
base = pd.read_csv('AirPassengers.csv', parse_dates = ['Month'], index_col='Month', date_parser = dateparse) # index_col - index vira data
#index vira data importante para série temporal.

ts=base['#Passengers'] # Saudavel transformar o tipo "dataframe" como series
plt.plot(ts)

#Prevendo através de Arima / Parâmetros p,q,d (devem ser feitos testes para qual melhor se adapta)

modelo = ARIMA(ts,order=(2,1,2)) # criar modelo ARIMA
modelo_treinado = modelo.fit() #treinando modelo
modelo_treinado.summary() # visualizar resumo do modelo

previsoes = modelo_treinado.forecast(steps=12) [0]# steps quantas previsoes eu quero [0] para apenas ver o resultado de previsoes

eixo = ts.plot() # plotar dados orignais
#adicionando previsões
modelo_treinado.plot_predict('1960-01-01','1962-01-01',ax=eixo, plot_insample = True) #plot predict plota previsoes e ax = adiciona (une variaveis em mesmo grafico), insample apenas facilita visualização

# Trabalhando com AUTOARRIMA e ajuda 
modelo_auto = auto_arima(ts,n=12,seasonal=True, trace = True) #escolhendo melhor param de p,q e d

modelo_auto.summary() # Visualizar melhores parâmetros "SARIMAX"

proximos_12 = modelo_auto.predict(n_periods=12) # prevendo futuro com auto_arrima

