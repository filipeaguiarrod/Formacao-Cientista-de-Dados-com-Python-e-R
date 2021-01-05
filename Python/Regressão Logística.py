# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 21:00:47 2020

@author: rodri
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt # gerar os gráficos 
from sklearn.linear_model import LogisticRegression # modelo de regressão linear

base = pd.read_csv('Eleicao.csv',sep=';') # Importar dados do CSV com separador

plt.scatter(base.DESPESAS,base.SITUACAO) #Gráfico de Dispersão com colunas pré definidas da base

base.describe() # summary dos dados 
np.corrcoef(base.DESPESAS, base.SITUACAO) # Correlação entre as variáveis

X = base.iloc[:,2].values # Variável com despesas coluna 2 em X
X = X.reshape(-1,1) # gerando matriz 
# alternativa p/ matriz X=X[:;np.newaxis]

y = base.iloc[:,1].values # Variavel c/ situacao 

modelo = LogisticRegression()
modelo.fit(X,y)

modelo.coef_
modelo.intercept_

plt.scatter(X,y) #Gráfico de Dispersão


# Testando modelo 8

X_teste = np.linspace(10,3000,100) # gerando 100 n°s aleatorios de 10 a 3000

#criando função sigmóide:

def model(x):
    return 1/ (1+np.exp(-x))
r = model(X_teste * modelo.coef_ + modelo.intercept_).ravel() # ravel passa de matriz para vetor
plt.plot(X_teste,r,color='red')

base_provisoes = pd.read_csv('NovosCandidatos.csv', sep = ';')

despesas = base_provisoes.iloc[:,1].values #criar variavel só de despesas
despesas = despesas.reshape(-1,1) # nao mexo na linha -1 e acrescento coluna +1
provisoes_teste = modelo.predict(despesas) # prever resultado