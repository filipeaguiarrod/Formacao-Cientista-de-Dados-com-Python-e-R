# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 18:14:36 2020

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

decomposicao = seasonal_decompose(ts) # decompõe a série temporal

tendencia = decomposicao.trend #variavel que obtem a tendencia (trend)
plt.plot(tendencia)

sazonal = decomposicao.seasonal
plt.plot(sazonal)

aleatorio = decomposicao.resid # o que sobrou da tendencia e sazonal
plt.plot(aleatorio)


# subplot(4(linhas que vou utilizarpara visualizar, 1 colunas de visualização, 1 ID posso juntar tudo com mesmo ID )
plt.subplot(4,1,2) # cria um ID se eu deixar o mesmo sobreescreve
plt.plot(ts, label='Original')
plt.legend(loc='best')

plt.subplot(4,1,2)
plt.plot(tendencia, label='Tendência')
plt.legend(loc='best')

plt.subplot(4,1,3)
plt.plot(sazonal, label='Sazonalidade')
plt.legend(loc='best')

plt.subplot(4,1,4)
plt.plot(aleatorio, label='Aleatório')
plt.legend(loc='best')
plt.tight_layout() # Ajustar layout para nao comer legenda