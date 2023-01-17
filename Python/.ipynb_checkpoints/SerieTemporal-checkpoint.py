# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 21:25:24 2020

@author: rodri
"""
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from datetime import datetime

base = pd.read_csv('AirPassengers.csv')

print(base.dtypes) # object tem que virar data

dateparse = lambda dates: pd.datetime.strptime(dates,'%Y-%m') # transformar objeto em data (ano-mes)
base = pd.read_csv('AirPassengers.csv', parse_dates = ['Month'], index_col='Month', date_parser = dateparse) # index_col - index vira data
#index vira data importante para série temporal.

base.index 
ts=base['#Passengers'] # Saudavel transformar o tipo "dataframe" como series

ts[1] #achar valor
ts['1949-02-1']
ts[datetime(1949,2,1)]
ts['1950-01-01':'1950-07-31'] # buscar por intervalo de index
ts[:'1950-07-31'] # tudo que estiver atrás de 1950 
ts['1950']# todos meses daquele ano

ts.index.max() #maior valor de index
ts.index.min() #menor valor de index

plt.plot(ts) # visualizar série temporal

tsano = ts.resample('A').sum() # nova amostra de ano A vem da formula resample agrupados por ano
plt.plot(tsano) # gráfico agrupado anual

tsmes = ts.groupby([lambda x: x.month]).sum() # agrupando por mês ignorando anos
plt.plot(tsmes) # grafico agrupado mensal

ts_datas = ts['1960-01-01':'1960-12-01']
plt.plot(ts_datas)