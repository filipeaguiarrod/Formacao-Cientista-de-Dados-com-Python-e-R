# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 18:35:56 2020

@author: rodri
"""

import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from statsmodels.tsa.seasonal import seasonal_decompose

base = pd.read_csv('AirPassengers.csv')
dateparse = lambda dates: pd.datetime.strptime(dates,'%Y-%m') # transformar objeto em data (ano-mes)
base = pd.read_csv('AirPassengers.csv', parse_dates = ['Month'], index_col='Month', date_parser = dateparse) # index_col - index vira data
#index vira data importante para série temporal.

ts=base['#Passengers'] # Saudavel transformar o tipo "dataframe" como series
plt.plot(ts)

#Primeira previsão Básica / Erro grande 

ts.mean() # media de todos registros

# Media apenas do ultimo ano

ts['1960-01-01':'1960-12-01'].mean()

#Medias moveis, utilizido 12 datas antes da que quero prever

mediamovel = ts.rolling(window = 12).mean() #media movel windows 12 ultimos

# 12 primeiros valores ficam nulos pois só consigo prever próximo com 12 valores.

# Comparando media móvel com série

plt.plot(ts, label='Original')
plt.legend(loc='best')

plt.plot(mediamovel, label='mediamovel')
plt.legend(loc='best')

#Prever próximas 12 meses com média movel:

previsoes=[]
for i in range (1,13): # Limitando o intervalo de média -12
    #print(i)
    superior = len(mediamovel)-i
    inferior = superior -11
    #print(inferior)
    #print(superior)
    #print('__________')
    previsoes.append(mediamovel[inferior:superior].mean())
    
    # esta em ordem inversa a previsão - corrigindo
previsoes = previsoes[::-1]
plt.plot(previsoes)
plt.plot(ts)