# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 20:41:13 2020

@author: rodri
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt # gerar os gráficos 
from sklearn.linear_model import LinearRegression # modelo de regressão linear 
from yellowbrick.regressor import ResidualsPlot

base = pd.read_csv('cars.csv') # puxar base csv e transformar em list
base = base.drop(['Unnamed: 0'], axis = 1 ) # excluir coluna 1 de dados

X = base.iloc[:,1].values # criar variável de 'distância' index = 1  - values coloca para valor
X= X.reshape(-1,1) # gerar matriz 
Y = base.iloc[:,0].values # Gerar Y como variável de 'speed'. O VALUE transforma para número

correlação = np.corrcoef(X,Y)

modelo = LinearRegression() # modelo ???
modelo.fit(X,Y)

modelo.intercept_
modelo.coef_

plt.scatter(X,Y) # pontos dos registros
plt.plot(X, modelo.predict(X),color='red') # algoritimo de ac

#distancia 22 pés ,qual VELOCIDADE ?

modelo.intercept_ + modelo.coef_*22 


modelo.predict([[22]])

modelo._residues

visualizador = ResidualsPlot(modelo)
visualizador.fit(X,Y)
visualizador.poof()